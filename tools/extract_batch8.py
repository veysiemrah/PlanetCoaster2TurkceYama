"""Batch 8: challenges + hint + newslettercountry + presettexture pending."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

# DIKKAT: prefix kontrolu - "challenges" "challenge" ile karismamali
exact_prefixes = [
    ("challenges_", "challenges"),
    ("hint_", "hint"),
    ("newslettercountry_", "newslettercountry"),
    ("presettexture_", "presettexture"),
]
buckets = {cat: [] for _, cat in exact_prefixes}

for k, v in strings.items():
    if v.get("status") == "translated":
        continue
    key_l = k.lower()
    for pre, cat in exact_prefixes:
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
Path("../translations/batch8_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Yazildi: translations/batch8_source.json")
