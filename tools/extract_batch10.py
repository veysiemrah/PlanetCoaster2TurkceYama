"""Batch 10: naturescene + filter + shop + water + newsletterlanguage pending."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

# Exclude longer overlapping prefixes
EXCLUDE = ["shopitem_", "newslettercountry_"]
EXACT = [
    ("naturescene_", "naturescene"),
    ("filter_", "filter"),
    ("newsletterlanguage_", "newsletterlanguage"),
    ("shop_", "shop"),
    ("water_", "water"),
]
buckets = {cat: [] for _, cat in EXACT}

for k, v in strings.items():
    if v.get("status") == "translated":
        continue
    key_l = k.lower()
    if any(key_l.startswith(ex) for ex in EXCLUDE):
        continue
    for pre, cat in EXACT:
        if key_l.startswith(pre):
            buckets[cat].append({
                "key": k,
                "source": v.get("source", ""),
                "context": v.get("context", ""),
                "max_length": v.get("max_length"),
            })
            break

for cat in buckets:
    print(f"{cat}: {len(buckets[cat])}")
print("Toplam:", sum(len(v) for v in buckets.values()))

out = {"items": [item for cat in buckets for item in buckets[cat]]}
Path("../translations/batch10_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Yazildi: translations/batch10_source.json")
