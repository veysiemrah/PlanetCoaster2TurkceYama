# Planet Coaster 2 Türkçe Yama MVP Implementasyon Planı

> **Agent çalışanlar için:** ZORUNLU ALT-SKILL: Bu planı görev görev implement etmek için superpowers:subagent-driven-development (önerilen) veya superpowers:executing-plans kullanın. Adımlar checkbox (`- [ ]`) syntax'ıyla takip edilir.

**Hedef:** Planet Coaster 2 için OVL extract → JSON çeviri → OVL build pipeline'ı kurma ve topluluk katılımlı çeviri altyapısını hazırlama.

**Mimari:** Python tabanlı 3 script (extract/validate/build) cobra-tools kütüphanesini sarmalar. Çevirmenler JSON dosyalarını düzenler, CI otomatik validate eder, release'de otomatik OVL build yapılır. Çekçe dili Türkçe olarak override edilir.

**Teknoloji Yığını:** Python 3.10+, cobra-tools (OpenNaja/cobra-tools), pytest, GitHub Actions, JSON

**Referans:** `docs/superpowers/specs/2026-04-13-turkce-yama-design.md`

---

## Görev 1: Proje İskeletini Oluştur

**Dosyalar:**
- Oluştur: `.gitignore`
- Oluştur: `README.md`
- Oluştur: `requirements.txt`

- [ ] **Adım 1: Git reposunu başlat**

```bash
cd "C:/Users/veysi/Projeler/PlanetCoaster2TurkceYama"
git init
git branch -m main
```

- [ ] **Adım 2: Temel dizin yapısını oluştur**

```bash
mkdir -p tools translations source output docs .github/workflows tests
```

- [ ] **Adım 3: .gitignore yaz**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
.env
*.egg-info/

# Build çıktıları
output/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# cobra-tools local clone
cobra-tools/
```

- [ ] **Adım 4: README.md yaz**

```markdown
# Planet Coaster 2 Türkçe Yama

Planet Coaster 2 için topluluk destekli, açık kaynaklı Türkçe çeviri yaması.

## Durum
🚧 Geliştirme aşamasında

## Kurulum
Bkz: [docs/INSTALL.md](docs/INSTALL.md)

## Katkıda Bulunma
Bkz: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)

## Lisans
MIT
```

- [ ] **Adım 5: requirements.txt yaz**

```
# cobra-tools GitHub'dan kurulur, aşağıdaki bağımlılıklarla birlikte
pytest>=7.0
pytest-cov>=4.0
```

- [ ] **Adım 6: Commit**

```bash
git add .gitignore README.md requirements.txt
git commit -m "chore: initialize project scaffolding"
```

---

## Görev 2: Python Sanal Ortamı ve cobra-tools Kurulumu

**Dosyalar:**
- Oluştur: `docs/DEVELOPMENT.md`

- [ ] **Adım 1: Python sanal ortamı oluştur ve aktifleştir**

```bash
cd "C:/Users/veysi/Projeler/PlanetCoaster2TurkceYama"
python -m venv venv
source venv/Scripts/activate
python --version
```
Beklenen: Python 3.10+ sürümü.

- [ ] **Adım 2: cobra-tools'u klonla**

```bash
git clone https://github.com/OpenNaja/cobra-tools.git
cd cobra-tools
git log -1 --oneline
```
Beklenen: Yakın tarihli bir commit.

- [ ] **Adım 3: cobra-tools bağımlılıklarını kur**

```bash
cd "C:/Users/veysi/Projeler/PlanetCoaster2TurkceYama"
pip install -r cobra-tools/requirements.txt
pip install -r requirements.txt
```

- [ ] **Adım 4: cobra-tools'un import edilebildiğini doğrula**

```bash
python -c "import sys; sys.path.insert(0, 'cobra-tools'); from modules.formats.OVL import OvlFile; print('OK')"
```
Beklenen: `OK` çıktısı.

- [ ] **Adım 5: DEVELOPMENT.md yaz**

```markdown
# Geliştirme Rehberi

## Gereksinimler
- Python 3.10+
- Git

## Kurulum
```bash
python -m venv venv
source venv/Scripts/activate  # Windows bash
# VEYA: venv\Scripts\activate.bat  # Windows cmd

git clone https://github.com/OpenNaja/cobra-tools.git
pip install -r cobra-tools/requirements.txt
pip install -r requirements.txt
```

## Araçlar
- `python tools/extract.py` — OVL'den JSON çıkart
- `python tools/validate.py` — çeviri doğrula
- `python tools/build.py` — JSON'dan OVL yap

## Test
```bash
pytest tests/
```
```

- [ ] **Adım 6: Commit**

```bash
git add docs/DEVELOPMENT.md
git commit -m "docs: add development setup guide"
```

---

## Görev 3: cobra-tools POC — Tek bir Loc.ovl Dosyasını Açma

**Dosyalar:**
- Oluştur: `tools/poc_read_ovl.py` (geçici, sonra silinecek)

- [ ] **Adım 1: POC scripti yaz**

```python
# tools/poc_read_ovl.py
"""cobra-tools ile bir Loc.ovl dosyasını açıp içindeki stringleri listeler."""
import sys
from pathlib import Path

# cobra-tools path
sys.path.insert(0, str(Path(__file__).parent.parent / "cobra-tools"))

from modules.formats.OVL import OvlFile
from generated.formats.ovl.versions import set_game


def main(ovl_path: str) -> None:
    ovl = OvlFile()
    set_game(ovl.context, "Planet Coaster 2")
    ovl.load(ovl_path)

    print(f"OVL yüklendi: {ovl_path}")
    print(f"Dosya sayısı: {len(ovl.files)}")

    txt_count = 0
    for f in ovl.files:
        if f.ext == ".txt":
            txt_count += 1
            if txt_count <= 5:
                print(f"  Örnek: {f.name} ({f.ext})")

    print(f"Toplam .txt dosyası: {txt_count}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python poc_read_ovl.py <ovl_path>")
        sys.exit(1)
    main(sys.argv[1])
```

- [ ] **Adım 2: POC scripti çalıştır**

```bash
python tools/poc_read_ovl.py "C:/XboxGames/Planet Coaster 2/Content/Win64/ovldata/Content0/Localised/English/UnitedKingdom/Loc.ovl"
```
Beklenen: "OVL yüklendi", dosya sayısı (birkaç bin), örnek .txt adları, toplam txt sayısı.

**Sorun giderme:** Hata alırsa cobra-tools dokümanlarına veya GitHub issue'larına bakın. `set_game` fonksiyonu için doğru string "Planet Coaster 2" olmalı (cobra-tools constants'ta kontrol edilebilir).

- [ ] **Adım 3: POC dosyasını sil**

```bash
rm tools/poc_read_ovl.py
```

Bu POC sadece cobra-tools entegrasyonunun çalıştığını doğrulamak içindi. Gerçek extract.py bir sonraki görevde yazılacak.

- [ ] **Adım 4: Commit (no-op marker)**

```bash
git commit --allow-empty -m "chore: verified cobra-tools works with PC2 OVL files"
```

---

## Görev 4: validate.py — JSON Schema Doğrulama (TDD)

**Dosyalar:**
- Oluştur: `tools/validate.py`
- Oluştur: `tests/test_validate_schema.py`
- Oluştur: `tests/fixtures/valid_translation.json`
- Oluştur: `tests/fixtures/invalid_missing_source.json`

- [ ] **Adım 1: Geçerli fixture dosyasını oluştur**

`tests/fixtures/valid_translation.json`:
```json
{
  "meta": {
    "language": "tr",
    "source_language": "en",
    "content_pack": "Content0",
    "game_version": "1.0.0",
    "last_updated": "2026-04-13"
  },
  "strings": {
    "UI_Test_Key": {
      "source": "Hello",
      "translation": "Merhaba",
      "status": "translated",
      "context": "Test",
      "max_length": null,
      "category": "ui_labels"
    }
  }
}
```

- [ ] **Adım 2: Hatalı fixture dosyasını oluştur**

`tests/fixtures/invalid_missing_source.json`:
```json
{
  "meta": {
    "language": "tr",
    "source_language": "en",
    "content_pack": "Content0",
    "game_version": "1.0.0",
    "last_updated": "2026-04-13"
  },
  "strings": {
    "UI_Test_Key": {
      "translation": "Merhaba",
      "status": "translated"
    }
  }
}
```

- [ ] **Adım 3: Başarısız testleri yaz**

`tests/test_validate_schema.py`:
```python
from pathlib import Path
from tools.validate import validate_schema, ValidationError

FIXTURES = Path(__file__).parent / "fixtures"


def test_valid_translation_passes():
    errors = validate_schema(FIXTURES / "valid_translation.json")
    assert errors == []


def test_missing_source_field_fails():
    errors = validate_schema(FIXTURES / "invalid_missing_source.json")
    assert len(errors) == 1
    assert "source" in errors[0].message
    assert errors[0].key == "UI_Test_Key"


def test_missing_file_raises():
    import pytest
    with pytest.raises(FileNotFoundError):
        validate_schema(FIXTURES / "nonexistent.json")


def test_invalid_json_raises():
    import pytest
    bad = FIXTURES / "bad.json"
    bad.write_text("{not valid json}", encoding="utf-8")
    try:
        with pytest.raises(ValueError):
            validate_schema(bad)
    finally:
        bad.unlink()
```

- [ ] **Adım 4: Testleri çalıştır ve başarısız olduklarını doğrula**

```bash
pytest tests/test_validate_schema.py -v
```
Beklenen: FAIL — `tools.validate` modülü yok.

- [ ] **Adım 5: validate.py'ın schema doğrulama kısmını yaz**

`tools/validate.py`:
```python
"""Türkçe yama çeviri dosyaları için doğrulama aracı."""
import json
from dataclasses import dataclass
from pathlib import Path


REQUIRED_STRING_FIELDS = ("source", "translation", "status")
VALID_STATUSES = ("untranslated", "translated", "needs_review")


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
                errors.append(ValidationError(
                    str(json_path), key, f"'{field}' alanı eksik"
                ))
        if "status" in entry and entry["status"] not in VALID_STATUSES:
            errors.append(ValidationError(
                str(json_path), key,
                f"Geçersiz status: {entry['status']}"
            ))

    return errors
```

- [ ] **Adım 6: Testleri çalıştır ve geçtiklerini doğrula**

```bash
pytest tests/test_validate_schema.py -v
```
Beklenen: 4 test PASS.

- [ ] **Adım 7: Commit**

```bash
git add tools/validate.py tests/test_validate_schema.py tests/fixtures/
git commit -m "feat(validate): add JSON schema validation"
```

---

## Görev 5: validate.py — Placeholder Koruma (TDD)

**Dosyalar:**
- Değiştir: `tools/validate.py`
- Oluştur: `tests/test_validate_placeholders.py`

- [ ] **Adım 1: Başarısız testleri yaz**

`tests/test_validate_placeholders.py`:
```python
from tools.validate import check_placeholders


def test_placeholder_preserved():
    errors = check_placeholders(
        key="UI_Score",
        source="Your score is {0}",
        translation="Puanın: {0}"
    )
    assert errors == []


def test_placeholder_missing_in_translation():
    errors = check_placeholders(
        key="UI_Score",
        source="Your score is {0}",
        translation="Puanın: "
    )
    assert len(errors) == 1
    assert "{0}" in errors[0]


def test_extra_placeholder_in_translation():
    errors = check_placeholders(
        key="UI_Score",
        source="Your score",
        translation="Puanın: {0}"
    )
    assert len(errors) == 1


def test_printf_style_preserved():
    errors = check_placeholders(
        key="K",
        source="Got %d items",
        translation="%d öğe alındı"
    )
    assert errors == []


def test_printf_style_missing():
    errors = check_placeholders(
        key="K",
        source="Got %d items",
        translation="öğe alındı"
    )
    assert len(errors) == 1
    assert "%d" in errors[0]
```

- [ ] **Adım 2: Testleri çalıştır ve başarısız olduklarını doğrula**

```bash
pytest tests/test_validate_placeholders.py -v
```
Beklenen: FAIL — `check_placeholders` fonksiyonu yok.

- [ ] **Adım 3: check_placeholders fonksiyonunu ekle**

`tools/validate.py` dosyasının sonuna ekle:
```python
import re

PLACEHOLDER_PATTERNS = [
    re.compile(r"\{\d+\}"),          # {0}, {1}, ...
    re.compile(r"\{[a-zA-Z_]+\}"),   # {name}
    re.compile(r"%[dsifx]"),         # %d, %s, %i, %f, %x
]


def check_placeholders(key: str, source: str, translation: str) -> list[str]:
    """Source'taki placeholder'ların translation'da korunup korunmadığını kontrol et.

    Returns: Hata mesajları listesi (boş = hepsi korunmuş).
    """
    errors: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        source_matches = set(pattern.findall(source))
        trans_matches = set(pattern.findall(translation))

        missing = source_matches - trans_matches
        extra = trans_matches - source_matches

        for m in missing:
            errors.append(f"{key}: çeviride eksik placeholder: {m}")
        for m in extra:
            errors.append(f"{key}: çeviride fazla placeholder: {m}")

    return errors
```

- [ ] **Adım 4: Testleri çalıştır**

```bash
pytest tests/test_validate_placeholders.py -v
```
Beklenen: 5 test PASS.

- [ ] **Adım 5: Commit**

```bash
git add tools/validate.py tests/test_validate_placeholders.py
git commit -m "feat(validate): add placeholder preservation check"
```

---

## Görev 6: validate.py — Glossary Tutarlılık Kontrolü (TDD)

**Dosyalar:**
- Değiştir: `tools/validate.py`
- Oluştur: `tests/test_validate_glossary.py`
- Oluştur: `tests/fixtures/test_glossary.json`

- [ ] **Adım 1: Test glossary fixture'ı oluştur**

`tests/fixtures/test_glossary.json`:
```json
{
  "terms": {
    "Coaster": {
      "translation": "Hız Treni",
      "note": "Test"
    },
    "Guest": {
      "translation": "Ziyaretçi",
      "note": "Test"
    }
  }
}
```

- [ ] **Adım 2: Başarısız testleri yaz**

`tests/test_validate_glossary.py`:
```python
from pathlib import Path
from tools.validate import check_glossary, load_glossary

FIXTURES = Path(__file__).parent / "fixtures"


def test_glossary_loaded():
    g = load_glossary(FIXTURES / "test_glossary.json")
    assert "Coaster" in g
    assert g["Coaster"]["translation"] == "Hız Treni"


def test_glossary_term_used_correctly():
    g = load_glossary(FIXTURES / "test_glossary.json")
    warnings = check_glossary(
        key="K",
        source="The Coaster is fast",
        translation="Hız Treni hızlıdır",
        glossary=g
    )
    assert warnings == []


def test_glossary_term_mistranslated():
    g = load_glossary(FIXTURES / "test_glossary.json")
    warnings = check_glossary(
        key="K",
        source="The Coaster is fast",
        translation="Lunapark treni hızlıdır",
        glossary=g
    )
    assert len(warnings) == 1
    assert "Coaster" in warnings[0]
    assert "Hız Treni" in warnings[0]


def test_glossary_irrelevant_term_ignored():
    g = load_glossary(FIXTURES / "test_glossary.json")
    warnings = check_glossary(
        key="K",
        source="Hello world",
        translation="Merhaba dünya",
        glossary=g
    )
    assert warnings == []
```

- [ ] **Adım 3: Testleri çalıştır ve başarısız olduklarını doğrula**

```bash
pytest tests/test_validate_glossary.py -v
```
Beklenen: FAIL — fonksiyonlar yok.

- [ ] **Adım 4: load_glossary ve check_glossary fonksiyonlarını ekle**

`tools/validate.py` dosyasının sonuna ekle:
```python
def load_glossary(path: Path) -> dict[str, dict]:
    """Glossary JSON dosyasını yükler."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data.get("terms", {})


def check_glossary(
    key: str, source: str, translation: str, glossary: dict[str, dict]
) -> list[str]:
    """Source'ta geçen glossary terimlerinin translation'da doğru karşılıkla kullanılıp
    kullanılmadığını kontrol et.

    Returns: Uyarı mesajları listesi.
    """
    warnings: list[str] = []
    source_lower = source.lower()
    translation_lower = translation.lower()

    for term, info in glossary.items():
        term_lower = term.lower()
        expected = info["translation"]
        expected_lower = expected.lower()

        if re.search(rf"\b{re.escape(term_lower)}\b", source_lower):
            if expected_lower not in translation_lower:
                warnings.append(
                    f"{key}: '{term}' terimi source'ta geçiyor, "
                    f"çeviride '{expected}' bekleniyor"
                )

    return warnings
```

- [ ] **Adım 5: Testleri çalıştır**

```bash
pytest tests/test_validate_glossary.py -v
```
Beklenen: 4 test PASS.

- [ ] **Adım 6: Commit**

```bash
git add tools/validate.py tests/test_validate_glossary.py tests/fixtures/test_glossary.json
git commit -m "feat(validate): add glossary consistency check"
```

---

## Görev 7: validate.py — İstatistik Raporu (TDD)

**Dosyalar:**
- Değiştir: `tools/validate.py`
- Oluştur: `tests/test_validate_stats.py`

- [ ] **Adım 1: Başarısız testi yaz**

`tests/test_validate_stats.py`:
```python
from pathlib import Path
from tools.validate import compute_stats

FIXTURES = Path(__file__).parent / "fixtures"


def test_stats_single_file():
    stats = compute_stats([FIXTURES / "valid_translation.json"])
    assert stats["total"] == 1
    assert stats["translated"] == 1
    assert stats["untranslated"] == 0
    assert stats["needs_review"] == 0
    assert stats["percent"] == 100.0


def test_stats_mixed(tmp_path):
    mixed = tmp_path / "mixed.json"
    mixed.write_text("""
{
  "meta": {"language": "tr", "source_language": "en", "content_pack": "X",
           "game_version": "1.0", "last_updated": "2026-04-13"},
  "strings": {
    "a": {"source": "A", "translation": "a", "status": "translated"},
    "b": {"source": "B", "translation": "", "status": "untranslated"},
    "c": {"source": "C", "translation": "c", "status": "needs_review"},
    "d": {"source": "D", "translation": "", "status": "untranslated"}
  }
}
""", encoding="utf-8")
    stats = compute_stats([mixed])
    assert stats["total"] == 4
    assert stats["translated"] == 1
    assert stats["untranslated"] == 2
    assert stats["needs_review"] == 1
    assert stats["percent"] == 25.0
```

- [ ] **Adım 2: Testi çalıştır ve başarısız olduğunu doğrula**

```bash
pytest tests/test_validate_stats.py -v
```
Beklenen: FAIL.

- [ ] **Adım 3: compute_stats fonksiyonunu ekle**

`tools/validate.py` dosyasının sonuna ekle:
```python
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
```

- [ ] **Adım 4: Testleri çalıştır**

```bash
pytest tests/test_validate_stats.py -v
```
Beklenen: 2 test PASS.

- [ ] **Adım 5: Commit**

```bash
git add tools/validate.py tests/test_validate_stats.py
git commit -m "feat(validate): add stats computation"
```

---

## Görev 8: validate.py — CLI Entry Point

**Dosyalar:**
- Değiştir: `tools/validate.py`

- [ ] **Adım 1: CLI main fonksiyonunu ekle**

`tools/validate.py` dosyasının sonuna ekle:
```python
import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Türkçe yama çeviri dosyalarını doğrula")
    parser.add_argument(
        "--translations-dir", default="translations",
        help="Çeviri JSON dosyalarının bulunduğu dizin"
    )
    parser.add_argument(
        "--glossary", default="glossary.json",
        help="Glossary JSON dosyası"
    )
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
        print(f"Toplam:        {stats['total']}")
        print(f"Çevrildi:      {stats['translated']} ({stats['percent']}%)")
        print(f"Çevrilmedi:    {stats['untranslated']}")
        print(f"İnceleme gerek: {stats['needs_review']}")
        return 0

    glossary = {}
    if Path(args.glossary).exists():
        glossary = load_glossary(Path(args.glossary))

    all_errors: list[str] = []
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

        if glossary:
            data = json.loads(jf.read_text(encoding="utf-8"))
            for key, entry in data.get("strings", {}).items():
                if entry.get("translation"):
                    g_warnings = check_glossary(
                        key, entry["source"], entry["translation"], glossary
                    )
                    all_errors.extend(f"{jf}: {w}" for w in g_warnings)

    if all_errors:
        for err in all_errors:
            print(err, file=sys.stderr)
        print(f"\n{len(all_errors)} sorun bulundu", file=sys.stderr)
        return 1

    print(f"Tüm çeviriler geçerli ({len(json_files)} dosya kontrol edildi)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Adım 2: CLI'yi manuel test et — boş dizin**

```bash
python tools/validate.py --stats
```
Beklenen: `UYARI: translations altında tr.json bulunamadı` veya istatistik (hepsi 0).

- [ ] **Adım 3: Tüm testleri çalıştır**

```bash
pytest tests/ -v
```
Beklenen: Tüm testler PASS.

- [ ] **Adım 4: Commit**

```bash
git add tools/validate.py
git commit -m "feat(validate): add CLI entry point"
```

---

## Görev 9: extract.py — Tek bir OVL'yi JSON'a Dönüştür

**Dosyalar:**
- Oluştur: `tools/extract.py`
- Oluştur: `tools/_cobra.py`

- [ ] **Adım 1: cobra-tools yardımcı modülünü yaz**

`tools/_cobra.py`:
```python
"""cobra-tools entegrasyonu için yardımcı modül."""
import sys
from pathlib import Path

COBRA_PATH = Path(__file__).parent.parent / "cobra-tools"
if str(COBRA_PATH) not in sys.path:
    sys.path.insert(0, str(COBRA_PATH))

from modules.formats.OVL import OvlFile  # noqa: E402
from generated.formats.ovl.versions import set_game  # noqa: E402

GAME_NAME = "Planet Coaster 2"


def load_ovl(ovl_path: Path) -> OvlFile:
    """Bir OVL dosyasını PC2 ayarlarıyla yükler."""
    ovl = OvlFile()
    set_game(ovl.context, GAME_NAME)
    ovl.load(str(ovl_path))
    return ovl


def extract_txt_entries(ovl: OvlFile, work_dir: Path) -> dict[str, str]:
    """OVL içindeki tüm .txt dosyalarını extract eder, {name: content} döndürür.

    work_dir geçici bir dizindir; cobra-tools extract için buna ihtiyaç duyar.
    """
    work_dir.mkdir(parents=True, exist_ok=True)
    ovl.extract(str(work_dir), only_types=[".txt"])

    entries: dict[str, str] = {}
    for txt_file in work_dir.rglob("*.txt"):
        rel_name = txt_file.stem
        try:
            content = txt_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = txt_file.read_text(encoding="latin-1")
        entries[rel_name] = content

    return entries
```

- [ ] **Adım 2: extract.py ana scriptini yaz**

`tools/extract.py`:
```python
"""Planet Coaster 2 Loc.ovl dosyalarını JSON'a dönüştürür."""
import argparse
import json
import sys
import tempfile
from datetime import date
from pathlib import Path

from _cobra import load_ovl, extract_txt_entries


CONTENT_PACKS = [
    "Content0", "Content1", "Content2", "Content3", "Content4",
    "Content5", "Content6", "Content7", "Content8",
    "ContentAnniversary", "ContentFestive",
    "ContentPDLC1", "ContentPDLC2", "ContentPDLC3",
]


def find_loc_ovl(game_dir: Path, pack: str, language: str = "English") -> Path | None:
    """Bir content paketi içindeki Loc.ovl dosyasını bulur."""
    base = game_dir / "Content" / "Win64" / "ovldata" / pack / "Localised" / language
    matches = list(base.rglob("Loc.ovl"))
    return matches[0] if matches else None


def extract_pack(game_dir: Path, pack: str, out_dir: Path) -> int:
    """Bir content paketinin İngilizce Loc.ovl'sini en.json'a dönüştürür.

    Returns: Çıkarılan string sayısı.
    """
    ovl_path = find_loc_ovl(game_dir, pack, "English")
    if not ovl_path:
        print(f"  {pack}: Loc.ovl bulunamadı, atlanıyor")
        return 0

    print(f"  {pack}: {ovl_path}")
    ovl = load_ovl(ovl_path)

    with tempfile.TemporaryDirectory() as tmp:
        entries = extract_txt_entries(ovl, Path(tmp))

    pack_dir = out_dir / pack
    pack_dir.mkdir(parents=True, exist_ok=True)

    data = {
        "meta": {
            "language": "en",
            "source_language": "en",
            "content_pack": pack,
            "game_version": "extracted",
            "last_updated": date.today().isoformat(),
        },
        "strings": {
            key: {
                "source": value,
                "translation": value,
                "status": "translated",
                "context": "",
                "max_length": None,
                "category": "",
            }
            for key, value in sorted(entries.items())
        },
    }

    out_file = pack_dir / "en.json"
    out_file.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"    -> {out_file} ({len(entries)} string)")
    return len(entries)


def main() -> int:
    parser = argparse.ArgumentParser(description="PC2 Loc.ovl dosyalarını JSON'a çıkar")
    parser.add_argument(
        "--game-dir", required=True,
        help="Planet Coaster 2 kurulum dizini (örn. C:/XboxGames/Planet Coaster 2)"
    )
    parser.add_argument("--output", default="source", help="Çıktı dizini")
    parser.add_argument(
        "--pack", help="Sadece belirli bir content paketi için çalıştır"
    )
    args = parser.parse_args()

    game_dir = Path(args.game_dir)
    if not game_dir.exists():
        print(f"HATA: {game_dir} bulunamadı", file=sys.stderr)
        return 1

    out_dir = Path(args.output)
    packs = [args.pack] if args.pack else CONTENT_PACKS

    total = 0
    for pack in packs:
        total += extract_pack(game_dir, pack, out_dir)

    print(f"\nToplam {total} string {out_dir} altına çıkarıldı.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Adım 3: Tek bir paket ile dene — Content0**

```bash
python tools/extract.py --game-dir "C:/XboxGames/Planet Coaster 2" --pack Content0
```
Beklenen: `source/Content0/en.json` oluşur, birkaç bin string içerir.

- [ ] **Adım 4: Oluşan dosyayı incele**

```bash
python -c "import json; d=json.load(open('source/Content0/en.json','r',encoding='utf-8')); print(f'Toplam: {len(d[chr(34)+chr(115)+chr(116)+chr(114)+chr(105)+chr(110)+chr(103)+chr(115)+chr(34)])}'); print('Örnek:', list(d['strings'].items())[0])"
```
Beklenen: Toplam string sayısı ve bir örnek string.

- [ ] **Adım 5: Commit**

```bash
git add tools/extract.py tools/_cobra.py
git commit -m "feat(extract): add OVL to JSON extraction"
```

---

## Görev 10: build.py — JSON'dan OVL Oluştur

**Dosyalar:**
- Oluştur: `tools/build.py`
- Değiştir: `tools/_cobra.py`

- [ ] **Adım 1: _cobra.py'a build helper'ı ekle**

`tools/_cobra.py` dosyasının sonuna ekle:
```python
def build_loc_ovl(
    entries: dict[str, str],
    template_ovl: Path,
    output_ovl: Path,
) -> None:
    """Bir {name: content} dictionary'sinden Loc.ovl dosyası oluşturur.

    template_ovl: Yapıyı referans almak için mevcut bir dil OVL'si (örn. Çekçe).
    """
    import tempfile

    ovl = load_ovl(template_ovl)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        ovl.extract(str(tmp_path), only_types=[".txt"])

        for txt_file in tmp_path.rglob("*.txt"):
            name = txt_file.stem
            if name in entries:
                txt_file.write_text(entries[name], encoding="utf-8")

        ovl2 = OvlFile()
        set_game(ovl2.context, GAME_NAME)
        ovl2.create(str(tmp_path))
        output_ovl.parent.mkdir(parents=True, exist_ok=True)
        ovl2.save(str(output_ovl))
```

- [ ] **Adım 2: build.py ana scriptini yaz**

`tools/build.py`:
```python
"""Türkçe JSON çevirilerinden Planet Coaster 2 mod paketleri oluşturur."""
import argparse
import json
import sys
from pathlib import Path

from _cobra import build_loc_ovl


CONTENT_PACKS = [
    "Content0", "Content1", "Content2", "Content3", "Content4",
    "Content5", "Content6", "Content7", "Content8",
    "ContentAnniversary", "ContentFestive",
    "ContentPDLC1", "ContentPDLC2", "ContentPDLC3",
]

MANIFEST_XML = """<?xml version="1.0" encoding="utf-8"?>
<ContentPack name="TurkceYama" version="1.0.0">
  <Description>Planet Coaster 2 Türkçe Çeviri Yaması</Description>
</ContentPack>
"""


def load_translations(json_path: Path) -> dict[str, str]:
    """tr.json'dan {key: translation} dictionary'si çıkarır (boş çeviriler source'u kullanır)."""
    data = json.loads(json_path.read_text(encoding="utf-8"))
    result: dict[str, str] = {}
    for key, entry in data.get("strings", {}).items():
        translation = entry.get("translation", "").strip()
        result[key] = translation if translation else entry.get("source", "")
    return result


def build_pack(
    pack: str,
    translations_dir: Path,
    game_dir: Path,
    output_dir: Path,
    target_language: str = "Czech",
    target_region: str = "CzechRepublic",
) -> bool:
    """Bir content paketi için Loc.ovl build eder."""
    tr_json = translations_dir / pack / "tr.json"
    if not tr_json.exists():
        print(f"  {pack}: tr.json bulunamadı, atlanıyor")
        return False

    template = (
        game_dir / "Content" / "Win64" / "ovldata" / pack / "Localised"
        / target_language / target_region / "Loc.ovl"
    )
    if not template.exists():
        print(f"  {pack}: Çekçe template bulunamadı ({template}), atlanıyor")
        return False

    entries = load_translations(tr_json)
    output_ovl = (
        output_dir / "TurkceYama" / "Main" / pack / "Localised"
        / target_language / target_region / "Loc.ovl"
    )
    print(f"  {pack}: {len(entries)} string -> {output_ovl}")
    build_loc_ovl(entries, template, output_ovl)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="JSON çevirilerinden PC2 mod paketi oluştur")
    parser.add_argument("--game-dir", required=True, help="PC2 kurulum dizini (template OVL için)")
    parser.add_argument("--translations-dir", default="translations")
    parser.add_argument("--output", default="output")
    parser.add_argument("--pack", help="Sadece belirli bir paket")
    args = parser.parse_args()

    game_dir = Path(args.game_dir)
    translations_dir = Path(args.translations_dir)
    output_dir = Path(args.output)

    manifest = output_dir / "TurkceYama" / "Manifest.xml"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(MANIFEST_XML, encoding="utf-8")

    packs = [args.pack] if args.pack else CONTENT_PACKS
    built = 0
    for pack in packs:
        if build_pack(pack, translations_dir, game_dir, output_dir):
            built += 1

    print(f"\n{built}/{len(packs)} paket build edildi. Çıktı: {output_dir}/TurkceYama/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Adım 3: Test için translations/Content0/tr.json oluştur**

```bash
mkdir -p translations/Content0
cp source/Content0/en.json translations/Content0/tr.json
python -c "
import json
d = json.load(open('translations/Content0/tr.json', 'r', encoding='utf-8'))
d['meta']['language'] = 'tr'
for k, v in d['strings'].items():
    v['translation'] = ''
    v['status'] = 'untranslated'
json.dump(d, open('translations/Content0/tr.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK')
"
```
Beklenen: `OK` çıktısı.

- [ ] **Adım 4: build.py'yi Content0 için çalıştır**

```bash
python tools/build.py --game-dir "C:/XboxGames/Planet Coaster 2" --pack Content0
```
Beklenen: `output/TurkceYama/Main/Content0/Localised/Czech/CzechRepublic/Loc.ovl` oluşur.

- [ ] **Adım 5: Çıktı dosyasını doğrula**

```bash
ls "output/TurkceYama/Main/Content0/Localised/Czech/CzechRepublic/"
```
Beklenen: `Loc.ovl` dosyası listeleniyor.

- [ ] **Adım 6: Commit (translations/ içeriğini commit etme — .gitkeep kullan)**

```bash
rm -rf translations/Content0  # Gerçek çeviri değil, test için oluşturulmuştu
git add tools/build.py tools/_cobra.py
git commit -m "feat(build): add JSON to OVL mod pack builder"
```

---

## Görev 11: Glossary.json Başlangıç Terimleri

**Dosyalar:**
- Oluştur: `glossary.json`

- [ ] **Adım 1: Başlangıç sözlüğünü yaz**

`glossary.json`:
```json
{
  "meta": {
    "version": "0.1.0",
    "last_updated": "2026-04-13",
    "description": "Planet Coaster 2 Türkçe Yama Terimler Sözlüğü"
  },
  "terms": {
    "Coaster": {
      "translation": "Hız Treni",
      "note": "'Roller coaster' kısaltması. 'Lunapark treni' kullanılmaz."
    },
    "Roller Coaster": {
      "translation": "Hız Treni",
      "note": "'Coaster' ile aynı çeviri."
    },
    "Guest": {
      "translation": "Ziyaretçi",
      "note": "Tema parkı bağlamı. 'Misafir' değil."
    },
    "Ride": {
      "translation": "Eğlence Birimi",
      "note": "Genel bir eğlence tesisi. Fiil olarak 'binmek' kullanılabilir."
    },
    "Scenery": {
      "translation": "Dekorasyon",
      "note": "Park süsleme öğeleri."
    },
    "Park": {
      "translation": "Park",
      "note": "Aynen korunur. 'Tema parkı' gerektiğinde açıklamada kullanılır."
    },
    "Staff": {
      "translation": "Personel",
      "note": "Çalışan kadrosu."
    },
    "Mechanic": {
      "translation": "Tamirci",
      "note": "Park çalışanı rolü."
    },
    "Janitor": {
      "translation": "Temizlikçi",
      "note": "Park çalışanı rolü."
    },
    "Entertainer": {
      "translation": "Animatör",
      "note": "Park çalışanı rolü. 'Eğlendirici' değil."
    },
    "Security": {
      "translation": "Güvenlik",
      "note": "Park çalışanı rolü."
    },
    "Queue": {
      "translation": "Sıra",
      "note": "Ride kuyruğu."
    },
    "Path": {
      "translation": "Yol",
      "note": "Park içi patika."
    },
    "Thrill": {
      "translation": "Heyecan",
      "note": "Ride istatistiği."
    },
    "Excitement": {
      "translation": "Eğlence",
      "note": "Ride istatistiği (Fun ≠ Excitement, dikkat)."
    },
    "Nausea": {
      "translation": "Mide Bulantısı",
      "note": "Ride istatistiği."
    },
    "Reliability": {
      "translation": "Güvenilirlik",
      "note": "Ride istatistiği."
    },
    "Prestige": {
      "translation": "Prestij",
      "note": "Park istatistiği."
    },
    "Shop": {
      "translation": "Dükkan",
      "note": "Satış noktası."
    },
    "Restaurant": {
      "translation": "Restoran"
    },
    "Facility": {
      "translation": "Tesis",
      "note": "Tuvalet, bilgi merkezi vb. yardımcı tesisler."
    },
    "Blueprint": {
      "translation": "Şablon",
      "note": "Kaydedilmiş tasarım. 'Blueprint' aynen korunabilir bazı bağlamlarda."
    },
    "Sandbox": {
      "translation": "Serbest Mod",
      "note": "Oyun modu."
    },
    "Career": {
      "translation": "Kariyer",
      "note": "Oyun modu."
    },
    "Franchise": {
      "translation": "Franchise",
      "note": "Oyun modu, aynen korunur."
    }
  }
}
```

- [ ] **Adım 2: validate.py ile glossary'yi test et**

```bash
python tools/validate.py --stats
```
Beklenen: Hata vermemeli (translations dizini boş).

- [ ] **Adım 3: Commit**

```bash
git add glossary.json
git commit -m "feat: add initial glossary with 25 core terms"
```

---

## Görev 12: Dokümantasyon — STYLE_GUIDE, CONTRIBUTING, INSTALL

**Dosyalar:**
- Oluştur: `docs/STYLE_GUIDE.md`
- Oluştur: `docs/CONTRIBUTING.md`
- Oluştur: `docs/INSTALL.md`

- [ ] **Adım 1: STYLE_GUIDE.md yaz**

`docs/STYLE_GUIDE.md`:
```markdown
# Çeviri Stil Rehberi

Tüm çevirmenlerin uyması gereken kurallar.

## Hitap
Oyuncuya **"sen"** diye hitap edilir (samimi, senli-benli).
- ✅ "Parkına yeni bir tesis ekle"
- ❌ "Parkınıza yeni bir tesis ekleyiniz"

## Tutarlılık
Aynı İngilizce terim her yerde aynı Türkçe karşılıkla çevrilir.
- Referans: [`glossary.json`](../glossary.json)
- Yeni terim eklemek PR ile onaya tabidir.

## Doğallık
Birebir çeviri yerine Türkçede doğal akan ifadeler tercih edilir.
- ✅ "Park popülerliği artıyor"
- ❌ "Park popülaritesi artmaktadır"

## Kültürel Uyarlama
Para birimi, ölçü birimi gibi öğelerde oyun mantığı korunur. Oyunun kendi para birimi ("$") çevrilmez.

## Kısaltmalar
UI öğelerinde Türkçe uzadığında kabul edilebilir kısaltmalar kullanılabilir. `max_length` alanı varsa ona uyun.

## Değişkenler (Placeholder'lar)
`{0}`, `{1}`, `{name}`, `%s`, `%d` gibi placeholder'lar **asla** değiştirilmez. Çevirmen bunları korumak zorundadır.
- Source: `You earned {0} coins`
- ✅ Çeviri: `{0} jeton kazandın`
- ❌ Çeviri: `0 jeton kazandın` (placeholder kayboldu)

## Büyük/Küçük Harf
Başlıklar için her kelimenin baş harfi büyük (Türkçe başlık kuralı).

## Kategori Üslup Kuralları

| Kategori | Üslup | Örnek |
|----------|-------|-------|
| `ui_buttons` | Kısa, emir kipi | "Oyna", "Kaydet" |
| `ui_labels` | Kısa, isim | "Ayarlar", "Gelir" |
| `ui_tooltips` | Açıklayıcı, 2. tekil şahıs | "Parkına yeni bir tesis ekle" |
| `descriptions` | Detaylı, resmi | Tesis açıklamaları |
| `tutorials` | Öğretici, samimi | Eğitim metinleri |
| `career_dialogue` | Doğal, konuşma dili | Kariyer diyalogları |

## Türkçe Karakter
Her zaman tam Türkçe karakter kullanın: `ç ğ ı ö ş ü`. `c g i o s u` gibi ASCII karakter kullanmayın.
```

- [ ] **Adım 2: CONTRIBUTING.md yaz**

`docs/CONTRIBUTING.md`:
```markdown
# Katkıda Bulunma Rehberi

## Nasıl Çevirmen Olurum?

1. Bu depoyu **fork** et
2. Kendi fork'unu **clone** et
3. `translations/<ContentPack>/tr.json` dosyasından çevirmek istediğin bir parça seç
4. `translation` alanlarını doldur, `status` alanını `translated` yap
5. Değişikliklerini **commit** et ve fork'una **push** et
6. **Pull request** aç

## Çeviri Kuralları

Çevirmeden önce mutlaka oku:
- [Stil Rehberi](STYLE_GUIDE.md)
- [glossary.json](../glossary.json) — Terimler sözlüğü

## Lokal Doğrulama

PR açmadan önce:
```bash
python tools/validate.py
```

İlerlemeni görmek için:
```bash
python tools/validate.py --stats
```

## PR Süreci

1. GitHub Actions otomatik `validate.py` çalıştırır
2. En az 1 maintainer çevirini inceler
3. Glossary ve stil rehberine uygunluk kontrol edilir
4. Onaylanan PR merge edilir

## Yeni Glossary Terimi Önerme

1. `glossary.json`'a terimi ekle (neden gerektiğini açıkla)
2. PR başlığı: `glossary: add <Term>`
3. PR açıklamasında terimin oyundaki bağlamını ve neden önerdiğin çeviriyi tercih ettiğini yaz

## İletişim

- GitHub Issues: Sorular, hata raporları
- Discord: (henüz yok)
```

- [ ] **Adım 3: INSTALL.md yaz**

`docs/INSTALL.md`:
```markdown
# Kurulum Rehberi

## Otomatik Kurulum (Windows)

1. [Releases](../../releases) sayfasından en son `TurkceYama-vX.Y.Z.zip` dosyasını indir
2. Zip'i çıkar
3. `install.bat` dosyasına çift tıkla
4. Script oyun dizinini bulur ve dosyaları kopyalar
5. Oyunu başlat, **Ayarlar > Dil** menüsünden **Čeština** seç
6. Oyun yeniden başladığında Türkçe görünür

## Manuel Kurulum

1. [Releases](../../releases) sayfasından `TurkceYama-vX.Y.Z.zip` dosyasını indir
2. Zip'i çıkar (içinden `TurkceYama/` klasörü çıkar)
3. Oyun kurulum dizinini bul:
   - **Xbox Game Pass:** `C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata\`
   - **Steam:** `C:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata\`
4. `TurkceYama/` klasörünü `ovldata/` dizinine kopyala
5. Oyunu başlat, **Ayarlar > Dil** menüsünden **Čeština** seç

## Neden Çekçe?

Oyunda yerleşik Türkçe dili olmadığı için Çekçe (Čeština) dili Türkçe ile değiştirilir. Oyun içinde dili "Čeština" seçtiğinde Türkçe görürsün.

## Yamayı Kaldırma

1. `ovldata/` dizininden `TurkceYama/` klasörünü sil
2. Oyunda dili tekrar istediğin dile değiştir

## Sorun Giderme

**Oyun açılmıyor:** `TurkceYama/` klasörünü sil, sorun devam ediyorsa oyun dosyalarını doğrula.

**Hala İngilizce:** Dil ayarının **Čeština** olduğundan emin ol. Oyunu kapatıp yeniden aç.

**Bazı metinler çevrilmemiş:** Çeviri devam ediyor. İlerleme için [README](../README.md) sayfasına bak.
```

- [ ] **Adım 4: Commit**

```bash
git add docs/STYLE_GUIDE.md docs/CONTRIBUTING.md docs/INSTALL.md
git commit -m "docs: add style guide, contributing, and install guides"
```

---

## Görev 13: install.bat Kurulum Scripti

**Dosyalar:**
- Oluştur: `install.bat`

- [ ] **Adım 1: install.bat yaz**

`install.bat`:
```batch
@echo off
setlocal enabledelayedexpansion

echo ============================================
echo  Planet Coaster 2 Turkce Yama Kurulum
echo ============================================
echo.

set "GAME_DIR="

rem Xbox Game Pass kontrol
if exist "C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata" (
    set "GAME_DIR=C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata"
    echo Xbox Game Pass kurulumu bulundu.
    goto :install
)

rem Steam kontrol
if exist "C:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata" (
    set "GAME_DIR=C:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata"
    echo Steam kurulumu bulundu.
    goto :install
)

echo Oyun kurulumu otomatik bulunamadi.
echo.
set /p "GAME_DIR=Lutfen ovldata dizini yolunu gir: "

if not exist "%GAME_DIR%" (
    echo HATA: %GAME_DIR% bulunamadi.
    pause
    exit /b 1
)

:install
echo.
echo Hedef: %GAME_DIR%
echo.

if not exist "TurkceYama" (
    echo HATA: TurkceYama klasoru bu dizinde bulunamadi.
    echo Bu script TurkceYama klasoru ile ayni dizinde olmali.
    pause
    exit /b 1
)

echo Yama kopyalaniyor...
xcopy /E /I /Y "TurkceYama" "%GAME_DIR%\TurkceYama"

if errorlevel 1 (
    echo HATA: Kopyalama basarisiz.
    pause
    exit /b 1
)

echo.
echo ============================================
echo  Kurulum tamamlandi!
echo ============================================
echo.
echo Simdi oyunu acip Ayarlar ^> Dil menusunden
echo "Cestina" secmelisin. Yama aktif olacak.
echo.
pause
```

- [ ] **Adım 2: Commit**

```bash
git add install.bat
git commit -m "feat: add Windows installation script"
```

---

## Görev 14: GitHub Actions — PR Doğrulama Workflow

**Dosyalar:**
- Oluştur: `.github/workflows/validate.yml`

- [ ] **Adım 1: validate.yml yaz**

`.github/workflows/validate.yml`:
```yaml
name: Validate Translations

on:
  pull_request:
    paths:
      - 'translations/**'
      - 'glossary.json'
      - 'tools/validate.py'
      - 'tests/**'
  push:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run unit tests
        run: pytest tests/ -v

      - name: Validate translations
        run: python tools/validate.py

      - name: Show stats
        if: always()
        run: python tools/validate.py --stats
```

- [ ] **Adım 2: Commit**

```bash
git add .github/workflows/validate.yml
git commit -m "ci: add PR validation workflow"
```

---

## Görev 15: Initial Extraction — İngilizce Kaynak Metinleri Çıkart ve Commit Et

**Dosyalar:**
- Oluştur: `source/**/en.json` (tüm content paketleri için)
- Oluştur: `translations/**/tr.json` (tüm content paketleri için, boş)

- [ ] **Adım 1: Tüm paketler için İngilizce extraction yap**

```bash
python tools/extract.py --game-dir "C:/XboxGames/Planet Coaster 2"
```
Beklenen: 15 content paketi için `source/<Pack>/en.json` dosyaları oluşur. Bazıları boş olabilir (Loc.ovl bulunmazsa atlanır).

- [ ] **Adım 2: Hangi paketlerin başarılı extraction yaptığını göster**

```bash
ls source/
```
Beklenen: Birden fazla paket dizini.

- [ ] **Adım 3: İlk tr.json iskeletlerini oluştur**

`tools/_init_translations.py` geçici scripti:
```python
"""İngilizce source'lardan boş Türkçe tr.json iskeletleri oluşturur."""
import json
from datetime import date
from pathlib import Path


def init_translations() -> None:
    source_dir = Path("source")
    translations_dir = Path("translations")

    for en_json in source_dir.rglob("en.json"):
        pack = en_json.parent.name
        tr_json = translations_dir / pack / "tr.json"
        tr_json.parent.mkdir(parents=True, exist_ok=True)

        data = json.loads(en_json.read_text(encoding="utf-8"))
        data["meta"]["language"] = "tr"
        data["meta"]["last_updated"] = date.today().isoformat()

        for entry in data["strings"].values():
            entry["translation"] = ""
            entry["status"] = "untranslated"

        tr_json.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"  {tr_json} oluşturuldu ({len(data['strings'])} string)")


if __name__ == "__main__":
    init_translations()
```

Çalıştır:
```bash
python tools/_init_translations.py
rm tools/_init_translations.py
```
Beklenen: Her paket için `translations/<Pack>/tr.json` oluşur.

- [ ] **Adım 4: Doğrulama ve istatistik**

```bash
python tools/validate.py --stats
```
Beklenen: Toplam string sayısı ve `%0.0` çeviri oranı.

- [ ] **Adım 5: Tüm testleri son kez çalıştır**

```bash
pytest tests/ -v
```
Beklenen: Tüm testler PASS.

- [ ] **Adım 6: Commit**

```bash
git add source/ translations/
git commit -m "feat: add extracted English sources and empty Turkish translations

$(python tools/validate.py --stats)"
```

---

## Self-Review Sonuçları

- **Spec kapsamı:** Tüm spec bölümleri görevlerde mevcut (tools, glossary, docs, CI, installer, mod yapısı)
- **Placeholder taraması:** TBD/TODO yok, tüm steplerde somut kod/komut var
- **Tip tutarlılığı:** Fonksiyon imzaları (`validate_schema`, `check_placeholders`, `check_glossary`, `compute_stats`, `load_ovl`, `extract_txt_entries`, `build_loc_ovl`) görevler arasında tutarlı

## Sonraki Adımlar (Bu Planın Dışında)

- **Release workflow (`release.yml`)**: Main'e merge'de otomatik build + GitHub Release
- **Topluluk oluşturma**: README'yi genişletme, Discord/issue template'leri
- **Gerçek çeviri çalışması**: Görev 15'te oluşan iskeletleri doldurma (topluluk işi)
- **Context zenginleştirme**: `context` alanlarını otomatik doldurma (path-based tahmin)
