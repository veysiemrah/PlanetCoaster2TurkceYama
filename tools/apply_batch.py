"""Generic batch applier: python apply_batch.py N (1..9)"""
import json
import shutil
import sys
from pathlib import Path

n = sys.argv[1] if len(sys.argv) > 1 else "1"
tr_path = Path("../translations/Content0/tr.json")
batch_path = Path(f"../translations/batch{n}_translated.json")
backup = tr_path.with_suffix(f".json.bak_batch{n}")

if not batch_path.exists():
    sys.exit(f"Yok: {batch_path}")

if not backup.exists():
    shutil.copy(tr_path, backup)
    print(f"Yedek: {backup.name}")

data = json.loads(tr_path.read_text(encoding="utf-8"))
batch = json.loads(batch_path.read_text(encoding="utf-8"))
strings = data["strings"]

applied = 0
missing = []
for category, items in batch.items():
    for key, translation in items.items():
        if key not in strings:
            missing.append(key)
            continue
        entry = strings[key]
        entry["translation"] = translation
        entry["status"] = "translated"
        entry["category"] = category
        applied += 1

tr_path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(f"Uygulanan: {applied}")
if missing:
    print(f"Bulunamayan {len(missing)}:")
    for k in missing[:20]:
        print(f"  {k}")
