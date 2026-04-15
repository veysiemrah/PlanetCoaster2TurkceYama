"""Türkçe yama çeviri dosyaları için doğrulama aracı."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_STRING_FIELDS = ("source", "translation", "status")
VALID_STATUSES = ("untranslated", "translated", "needs_review")

PLACEHOLDER_PATTERNS = [
    re.compile(r"\{\d+\}"),
    re.compile(r"\{[a-zA-Z_]+\}"),
    re.compile(r"%[dsifx]"),
]

# Glossary kontrolünden hariç tutulan anahtar desenleri.
# Bu anahtarlar asset adı, kredi, teknik bind gibi çevrilmeyen/kasıtlı korunan içeriklerdir.
GLOSSARY_SKIP_KEY_PATTERNS = [
    re.compile(r"^buildingpartname_"),
    re.compile(r"^guestname_"),
    re.compile(r"^credits_chunk_"),
    re.compile(r"^music_track_"),
    re.compile(r"^optionsmenu_controls_.*_input_"),
    re.compile(r"^shopitem_misc_(airmattress|poolinflatable|pool(pass|ring)|rubberring|ridephoto|waternoodle)"),
    re.compile(r"^frontendmenu_(scenarioname|setname)_"),   # senaryo/zone adları
    re.compile(r"^contentname_"),                           # içerik paketi adları (marketing)
    re.compile(r"^infopanel_(group_)?tolerances?_(will|not|less|no)"),  # Ride fiil formu
    re.compile(r"^sequence_fr_"),                           # animasyon dizisi adları
    re.compile(r"^tag_pdlc_"),                              # PDLC tag'leri (çevrilmiyor)
]

# Glossary kontrolü öncesi source/translation'dan çıkarılacak teknik tag/markup desenleri.
# [sentiment=Fear], {NodeName}, <h1>..</h1> vs. glossary karşılaştırmasına dahil edilmez.
TECHNICAL_TAG_PATTERNS = [
    re.compile(r"\[sentiment=[^\]]+\]"),
    re.compile(r"\[[a-zA-Z_]+=[^\]]+\]"),
    re.compile(r"<[^>]+>"),
    re.compile(r"\{[^}]+\}"),
]

# Glossary kontrolü öncesi source'ta maskelenecek özel ad/marka desenleri.
# "Planet Coaster" önceki oyun adı — "Coaster" burada Hız Treni olarak çevrilmez.
PROPER_NOUN_PATTERNS = [
    re.compile(r"\bPlanet Coaster\b"),
    re.compile(r"\bKing Coaster\b"),
    re.compile(r"\bCoaster Canyon\b"),
    re.compile(r"\bCoaster Coast\b"),
    re.compile(r"\bCoaster Park(land)?\b"),
    re.compile(r"\bCrimson Coaster\b"),
]


def _tr_casefold(text: str) -> str:
    """Türkçe-duyarlı lowercase. Python'un .lower() 'İ' için combining dot üretir
    ('İstasyon' → 'i̇stasyon'), TR içerikteki düz 'istasyon' ile eşleşmez.
    Bu fonksiyon I→ı, İ→i manuel dönüşümüyle bu bug'ı engeller.
    """
    return text.replace("İ", "i").replace("I", "ı").lower()

# Çeviride kesinlikle kullanılmaması gereken terimler → [HATA]
FORBIDDEN_TERMS: dict[str, str] = {
    "çekici": "Eğlence Birimi veya Aktivite",
    "misafir": "Ziyaretçi",
    "lunapark treni": "Hız Treni",
}

# Yazılı Türkçede kullanılmaması gereken ağız/argo sözcükler → [UYARI]
COLLOQUIAL_TERMS: list[str] = [
    "valla",
    "yahu",
    "pes artık",
    "yeter yahu",
]


@dataclass
class ValidationError:
    file: str
    key: str
    message: str


def validate_schema(json_path: Path) -> list[ValidationError]:
    """Bir çeviri JSON dosyasının şemasını doğrular.

    Returns: ValidationError listesi (boş = geçerli).
    Raises: FileNotFoundError, ValueError (JSON parse hatası).
    """
    json_path = Path(json_path)
    if not json_path.exists():
        raise FileNotFoundError(json_path)

    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON parse hatası: {e}") from e

    errors: list[ValidationError] = []
    if "strings" not in data:
        errors.append(ValidationError(str(json_path), "", "'strings' bölümü eksik"))
        return errors

    for key, entry in data["strings"].items():
        for field in REQUIRED_STRING_FIELDS:
            if field not in entry:
                errors.append(
                    ValidationError(str(json_path), key, f"'{field}' alanı eksik")
                )
        if "status" in entry and entry["status"] not in VALID_STATUSES:
            errors.append(
                ValidationError(
                    str(json_path), key, f"Geçersiz status: {entry['status']}"
                )
            )

    return errors


def check_placeholders(key: str, source: str, translation: str) -> list[str]:
    """Source'taki placeholder'ların translation'da korunup korunmadığını kontrol et."""
    errors: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        source_matches = set(pattern.findall(source))
        trans_matches = set(pattern.findall(translation))

        for m in source_matches - trans_matches:
            errors.append(f"{key}: çeviride eksik placeholder: {m}")
        for m in trans_matches - source_matches:
            errors.append(f"{key}: çeviride fazla placeholder: {m}")

    return errors


def check_forbidden_terms(key: str, translation: str) -> list[str]:
    """Çeviride yasaklı terimlerin kullanılıp kullanılmadığını kontrol et.

    Tam kelime eşleşmesi kullanır: 'çekici' aramak 'çekicilik'i eşleştirmez.

    Returns: Hata mesajı listesi (boş = temiz).
    """
    errors: list[str] = []
    for term, suggestion in FORBIDDEN_TERMS.items():
        pattern = r"\b" + re.escape(term) + r"\b"
        if re.search(pattern, translation, re.IGNORECASE):
            errors.append(
                f"{key}: yasaklı terim '{term}' — kullan: '{suggestion}'"
            )
    return errors


def check_colloquial_terms(key: str, translation: str) -> list[str]:
    """Çeviride argo/ağız sözcüklerini tespit et.

    Returns: Uyarı mesajı listesi (boş = temiz). Uyarı = hata değil.
    """
    warnings: list[str] = []
    translation_lower = translation.lower()
    for term in COLLOQUIAL_TERMS:
        if term.lower() in translation_lower:
            warnings.append(
                f"{key}: argo/ağız sözcüğü '{term}' — yazılı Türkçede kullanılmaz"
            )
    return warnings


def load_glossary(path: Path) -> dict[str, dict]:
    """Glossary JSON dosyasını yükler."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data.get("terms", {})


def _strip_technical_tags(text: str) -> str:
    """Teknik tagları boşlukla değiştir (offset korunur, kelime sınırları bozulmaz)."""
    for pat in TECHNICAL_TAG_PATTERNS:
        text = pat.sub(lambda m: " " * len(m.group(0)), text)
    return text


def _mask_proper_nouns(text: str) -> str:
    """Özel ad/marka ifadelerini boşlukla maskele (source için)."""
    for pat in PROPER_NOUN_PATTERNS:
        text = pat.sub(lambda m: " " * len(m.group(0)), text)
    return text


def check_glossary(
    key: str,
    source: str,
    translation: str,
    glossary: dict[str, dict],
) -> list[str]:
    """Source'ta geçen glossary terimlerinin translation'da doğru karşılıkla kullanılıp
    kullanılmadığını kontrol et.

    Kurallar:
    - Büyük/küçük harfe duyarlı: "Ride" sadece isim olarak (büyük harf) tetiklenir.
    - Uzun terimler önce eşleştirilir, eşleşen source bölgesi maskelenir → kısa terim
      aynı metne tekrar uyarı üretmez (örn. "Spinning Ride" eşleşince "Ride" tetiklenmez).
    - [sentiment=X], {placeholder}, <html> gibi teknik etiketler karşılaştırmaya dahil edilmez.
    - GLOSSARY_SKIP_KEY_PATTERNS'e uyan anahtarlar (asset/kredi/bind) tamamen atlanır.
    """
    for skip_pat in GLOSSARY_SKIP_KEY_PATTERNS:
        if skip_pat.search(key):
            return []

    warnings: list[str] = []
    source_clean = _mask_proper_nouns(_strip_technical_tags(source))
    translation_lower = _tr_casefold(_strip_technical_tags(translation))

    # Uzun glossary terimleri önce: "Spinning Ride" > "Ride"
    sorted_terms = sorted(glossary.items(), key=lambda kv: -len(kv[0]))

    # Mutable buffer: eşleşen bölgeleri boşlukla maskeleyeceğiz
    src_buf = list(source_clean)

    for term, info in sorted_terms:
        expected = info["translation"]
        # "Tren|Araç" gibi alternatifler: | ile ayır, herhangi biri eşleşirse geçer.
        expected_alts = [_tr_casefold(alt.strip()) for alt in expected.split("|")]

        pattern = re.compile(rf"\b{re.escape(term)}\b")
        current = "".join(src_buf)
        matches = list(pattern.finditer(current))
        if not matches:
            continue

        if not any(alt in translation_lower for alt in expected_alts):
            warnings.append(
                f"{key}: '{term}' terimi source'ta geçiyor, "
                f"çeviride '{expected}' bekleniyor"
            )

        # Eşleşen bölgeleri maskele → daha kısa terimler bu bölgeye denk gelmesin
        for m in matches:
            for i in range(m.start(), m.end()):
                src_buf[i] = " "

    return warnings


def compute_stats(json_paths: list[Path]) -> dict:
    """Birden fazla çeviri dosyasından toplam istatistik çıkarır."""
    total = translated = untranslated = needs_review = 0

    for path in json_paths:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        for entry in data.get("strings", {}).values():
            total += 1
            status = entry.get("status", "untranslated")
            if status == "translated":
                translated += 1
            elif status == "needs_review":
                needs_review += 1
            else:
                untranslated += 1

    percent = (translated / total * 100.0) if total else 0.0
    return {
        "total": total,
        "translated": translated,
        "untranslated": untranslated,
        "needs_review": needs_review,
        "percent": round(percent, 1),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Türkçe yama çeviri dosyalarını doğrula")
    parser.add_argument("--translations-dir", default="translations")
    parser.add_argument("--glossary", default="glossary.json")
    parser.add_argument("--stats", action="store_true", help="Sadece istatistik göster")
    parser.add_argument("--check-glossary", action="store_true", help="Sadece glossary kontrolü")
    args = parser.parse_args()

    translations_dir = Path(args.translations_dir)
    json_files = sorted(translations_dir.rglob("tr.json"))

    if not json_files:
        print(f"UYARI: {translations_dir} altında tr.json bulunamadı", file=sys.stderr)
        return 0

    if args.stats:
        stats = compute_stats(json_files)
        print(f"Toplam:         {stats['total']}")
        print(f"Çevrildi:       {stats['translated']} (%{stats['percent']})")
        print(f"Çevrilmedi:     {stats['untranslated']}")
        print(f"İnceleme gerek: {stats['needs_review']}")
        return 0

    glossary: dict[str, dict] = {}
    if Path(args.glossary).exists():
        glossary = load_glossary(Path(args.glossary))

    all_errors: list[str] = []
    all_warnings: list[str] = []
    for jf in json_files:
        schema_errors = validate_schema(jf)
        for e in schema_errors:
            all_errors.append(f"{e.file}: {e.key}: {e.message}")

        if not schema_errors and not args.check_glossary:
            data = json.loads(jf.read_text(encoding="utf-8"))
            for key, entry in data.get("strings", {}).items():
                if entry.get("translation"):
                    ph_errors = check_placeholders(
                        key, entry["source"], entry["translation"]
                    )
                    all_errors.extend(f"{jf}: {e}" for e in ph_errors)

                    fb_errors = check_forbidden_terms(key, entry["translation"])
                    all_errors.extend(f"[HATA]   {jf}: {e}" for e in fb_errors)

                    cq_warnings = check_colloquial_terms(key, entry["translation"])
                    all_warnings.extend(f"[UYARI]  {jf}: {w}" for w in cq_warnings)

        if glossary and not schema_errors:
            data = json.loads(jf.read_text(encoding="utf-8"))
            for key, entry in data.get("strings", {}).items():
                if entry.get("translation"):
                    g_warnings = check_glossary(
                        key, entry["source"], entry["translation"], glossary
                    )
                    all_errors.extend(f"{jf}: {w}" for w in g_warnings)

    if all_warnings:
        for w in all_warnings:
            print(w)

    if all_errors:
        for err in all_errors:
            print(err, file=sys.stderr)
        print(f"\n{len(all_errors)} hata bulundu", file=sys.stderr)
        return 1

    msg = f"Tüm çeviriler geçerli ({len(json_files)} dosya kontrol edildi)"
    if all_warnings:
        msg += f" — {len(all_warnings)} uyarı (argo sözcük)"
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
