"""Credits 45 HTML chunk'ini oldugu gibi (English) olarak 'translated' isaretle.

Bu, endustri pratigi: oyun credits'i kisi adlari ve rol unvanlari icerdiginden
ceviri yapilmaz, orijinal haliyle gosterilir.
"""
import json
import shutil
from pathlib import Path

tr_path = Path("../translations/Content0/tr.json")
backup = tr_path.with_suffix(".json.bak_credits")

if not backup.exists():
    shutil.copy(tr_path, backup)
    print(f"Yedek: {backup.name}")

data = json.loads(tr_path.read_text(encoding="utf-8"))
strings = data["strings"]

applied = 0
for k, v in strings.items():
    if v.get("status") == "translated":
        continue
    if not k.lower().startswith("credits"):
        continue
    v["translation"] = v.get("source", "")
    v["status"] = "translated"
    if not v.get("category"):
        v["category"] = "credits"
    applied += 1

tr_path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(f"Credits olarak isaretlenen: {applied}")
