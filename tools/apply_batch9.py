"""Batch 9 applier."""
import json
import shutil
from pathlib import Path

tr_path = Path("../translations/Content0/tr.json")
batch_path = Path("../translations/batch9_translated.json")
backup = tr_path.with_suffix(".json.bak_batch9")

if not backup.exists():
    shutil.copy(tr_path, backup)
    print(f"Yedek: {backup.name}")

data = json.loads(tr_path.read_text(encoding="utf-8"))
batch = json.loads(batch_path.read_text(encoding="utf-8"))
strings = data["strings"]

CATEGORY_MAP = [
    ("keplerrequesterror_", "keplerrequesterror"),
    ("trackelementdisabled_", "trackelementdisabled"),
    ("set_", "set"),
    ("challenge_", "challenge"),
]

applied = 0
missing = []
for item in batch["items"]:
    key = item["key"]
    translation = item["translation"]
    if key not in strings:
        missing.append(key)
        continue
    entry = strings[key]
    entry["translation"] = translation
    entry["status"] = "translated"
    if not entry.get("category"):
        key_l = key.lower()
        for pre, cat in CATEGORY_MAP:
            if key_l.startswith(pre):
                entry["category"] = cat
                break
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
