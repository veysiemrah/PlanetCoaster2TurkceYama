"""Batch 11: trackedit + friendshub + month + presence + trackfeature + time pending."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

EXCLUDE = ["trackeditparam_", "trackelementdisabled_", "trackelementname_", "trackelementdesc_", "triggeredaudioevents_", "triggeredsfx_"]
EXACT = [
    ("trackedit_", "trackedit"),
    ("friendshub_", "friendshub"),
    ("month_", "month"),
    ("presence_", "presence"),
    ("trackfeature_", "trackfeature"),
    ("time_", "time"),
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
Path("../translations/batch11_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Yazildi: translations/batch11_source.json")
