"""Generic batch validator: python validate_batch_generic.py N"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import check_glossary, load_glossary

n = sys.argv[1] if len(sys.argv) > 1 else "13"

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
batch = json.loads(Path(f"../translations/batch{n}_translated.json").read_text(encoding="utf-8"))
glossary = load_glossary(Path("../glossary.json"))

batch_keys = {item["key"] for item in batch["items"]}

issues = []
for key in batch_keys:
    entry = data["strings"].get(key)
    if not entry:
        continue
    ws = check_glossary(key, entry["source"], entry["translation"], glossary)
    for w in ws:
        issues.append(w)

print(f"Batch{n} anahtar sayisi: {len(batch_keys)}")
print(f"Uyari: {len(issues)}")
for w in issues:
    print(f"  {w}")
