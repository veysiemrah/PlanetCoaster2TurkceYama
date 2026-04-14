"""Kopyalanan OVL dosyasının string içeriğini doğrula."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _cobra import extract_ovl_txt

ovl = Path("C:/XboxGames/Planet Coaster 2/Content/Win64/ovldata/ContentPDLC1/Localised/English/UnitedKingdom/Loc.ovl")
tmp = tempfile.mkdtemp()
out = Path(tmp) / "check"
extract_ovl_txt(ovl, out)
files = list(out.rglob("*.txt"))
print(f"{len(files)} txt dosyasi bulundu")
for f in sorted(files)[:20]:
    content = f.read_text(encoding="utf-8")[:80]
    print(f"  {f.stem}: {content}")
