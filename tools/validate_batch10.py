"""Sadece batch10'da yer alan anahtarlari validate eder."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import check_glossary, load_glossary

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
batch = json.loads(Path("../translations/batch10_translated.json").read_text(encoding="utf-8"))
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

print(f"Batch10 anahtar sayisi: {len(batch_keys)}")
print(f"Uyari: {len(issues)}")
for w in issues:
    print(f"  {w}")
