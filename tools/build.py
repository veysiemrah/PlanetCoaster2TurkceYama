"""Türkçe JSON çevirilerinden Planet Coaster 2 mod paketi oluşturur."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

from _cobra import build_ovl_from_dir, extract_ovl_txt

CONTENT_PACKS = [
    "Content0", "Content1", "Content2", "Content3", "Content4",
    "Content5", "Content6", "Content7", "Content8",
    "ContentAnniversary", "ContentFestive",
    "ContentPDLC1", "ContentPDLC2", "ContentPDLC3",
]

TARGET_LANGUAGE = "Czech"
TARGET_REGION = "CzechRepublic"

MANIFEST_XML = """<?xml version="1.0" encoding="utf-8"?>
<ContentPack name="TurkceYama" version="1.0.0">
  <Description>Planet Coaster 2 Turkce Ceviri Yamasi</Description>
</ContentPack>
"""


def load_translations(json_path: Path) -> dict[str, str]:
    """tr.json'dan {key: translation} çıkarır.

    Boş çeviriler için source fallback kullanılır (eksik metin yerine İngilizce görünür).
    """
    data = json.loads(json_path.read_text(encoding="utf-8"))
    result: dict[str, str] = {}
    for key, entry in data.get("strings", {}).items():
        translation = (entry.get("translation") or "").strip()
        result[key] = translation if translation else entry.get("source", "")
    return result


def find_template_ovl(game_dir: Path, pack: str) -> Path | None:
    """Hedef dil (Çekçe) Loc.ovl'sini bulur — build için template olarak kullanılır."""
    base = (
        game_dir / "Content" / "Win64" / "ovldata" / pack / "Localised"
        / TARGET_LANGUAGE / TARGET_REGION
    )
    ovl = base / "Loc.ovl"
    return ovl if ovl.exists() else None


def build_pack(
    pack: str,
    translations_dir: Path,
    game_dir: Path,
    output_dir: Path,
) -> bool:
    """Bir content paketi için Türkçe Loc.ovl build eder."""
    tr_json = translations_dir / pack / "tr.json"
    if not tr_json.exists():
        print(f"  {pack}: tr.json bulunamadı, atlanıyor")
        return False

    template = find_template_ovl(game_dir, pack)
    if not template:
        print(f"  {pack}: Çekçe template bulunamadı, atlanıyor")
        return False

    translations = load_translations(tr_json)
    output_ovl = (
        output_dir / "TurkceYama" / "Main" / pack / "Localised"
        / TARGET_LANGUAGE / TARGET_REGION / "Loc.ovl"
    )

    print(f"  {pack}: {len(translations)} string -> {output_ovl.name}")
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "work"
        extract_ovl_txt(template, work)

        for txt_file in work.rglob("*.txt"):
            name = txt_file.stem
            if name in translations:
                txt_file.write_text(translations[name], encoding="utf-8")

        build_ovl_from_dir(work, output_ovl)

    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="JSON çevirilerinden PC2 mod paketi oluştur"
    )
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

    print(
        f"\n{built}/{len(packs)} paket build edildi. "
        f"Çıktı: {output_dir}/TurkceYama/"
    )
    return 0 if built > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
