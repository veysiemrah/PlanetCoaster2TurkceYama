"""Batch 12: triggeredsfx + parkzone + taggroup + tooltip + keplerrequesterrortext + park pending."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

EXCLUDE = ["triggeredaudioevents_", "parkmanagement_", "parkexpansion_"]
EXACT = [
    ("triggeredsfx_", "triggeredsfx"),
    ("parkzone_", "parkzone"),
    ("taggroup_", "taggroup"),
    ("tooltip_", "tooltip"),
    ("keplerrequesterrortext_", "keplerrequesterrortext"),
    ("keplerrequesterrortitle_", "keplerrequesterrortitle"),
    ("park_", "park"),
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
Path("../translations/batch12_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Yazildi: translations/batch12_source.json")
