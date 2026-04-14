"""batch1_translated.json -> tr.json'a uygular."""
import json
import shutil
from pathlib import Path

tr_path = Path("../translations/Content0/tr.json")
batch_path = Path("../translations/batch1_translated.json")
backup = tr_path.with_suffix(".json.bak_batch1")

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
    print(f"Bulunamayan {len(missing)} anahtar:")
    for k in missing[:20]:
        print(f"  {k}")
