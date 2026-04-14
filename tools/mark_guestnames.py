"""guestname kayitlarini kaynak=hedef olarak 'translated' isaretle.

Ziyaretci isimleri uluslararasi havuzdan rastgele secildigi icin
(Alice Zaytseva, John Wickrama vs.) cevrilmiyor. Bu script onlari
pending kuyrugundan dusurur.
"""
import json
import shutil
from pathlib import Path

tr_path = Path("../translations/Content0/tr.json")
backup = tr_path.with_suffix(".json.bak_guestname")

# Yedek (yoksa)
if not backup.exists():
    shutil.copy(tr_path, backup)
    print(f"Yedek olusturuldu: {backup.name}")

data = json.loads(tr_path.read_text(encoding="utf-8"))
strings = data["strings"]

updated = 0
for key, entry in strings.items():
    if not key.startswith("guestname"):
        continue
    if entry.get("status") == "translated":
        continue
    entry["translation"] = entry["source"]
    entry["status"] = "translated"
    entry["category"] = "guestname"
    updated += 1

tr_path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print(f"Guncellenen kayit: {updated}")
