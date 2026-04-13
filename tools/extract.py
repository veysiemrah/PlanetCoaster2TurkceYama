"""Planet Coaster 2 Loc.ovl dosyalarını JSON'a dönüştürür."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path

from _cobra import extract_ovl_txt

CONTENT_PACKS = [
    "Content0", "Content1", "Content2", "Content3", "Content4",
    "Content5", "Content6", "Content7", "Content8",
    "ContentAnniversary", "ContentFestive",
    "ContentPDLC1", "ContentPDLC2", "ContentPDLC3",
]

SOURCE_LANGUAGE = "English"
SOURCE_REGION = "UnitedKingdom"


def find_loc_ovl(game_dir: Path, pack: str) -> Path | None:
    """Bir content paketi içindeki İngilizce Loc.ovl dosyasını bulur."""
    base = (
        game_dir / "Content" / "Win64" / "ovldata" / pack
        / "Localised" / SOURCE_LANGUAGE
    )
    if not base.exists():
        return None
    matches = list(base.rglob("Loc.ovl"))
    return matches[0] if matches else None


def extract_pack(game_dir: Path, pack: str, out_dir: Path) -> int:
    """Bir content paketinin İngilizce Loc.ovl'sini en.json'a dönüştürür.

    Returns: Çıkarılan string sayısı (0 = paket atlandı).
    """
    ovl_path = find_loc_ovl(game_dir, pack)
    if not ovl_path:
        print(f"  {pack}: Loc.ovl bulunamadı, atlanıyor")
        return 0

    print(f"  {pack}: extract ediliyor... ({ovl_path.name})")
    with tempfile.TemporaryDirectory() as tmp:
        entries = extract_ovl_txt(ovl_path, Path(tmp))

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
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"    -> {out_file} ({len(entries)} string)")
    return len(entries)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="PC2 Loc.ovl dosyalarını JSON'a çıkar"
    )
    parser.add_argument(
        "--game-dir", required=True,
        help='PC2 kurulum dizini (örn. "C:/XboxGames/Planet Coaster 2")',
    )
    parser.add_argument("--output", default="source", help="Çıktı dizini (varsayılan: source)")
    parser.add_argument(
        "--pack",
        help="Sadece belirli bir content paketi için çalıştır (örn. Content0)",
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
