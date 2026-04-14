"""Batch 6: frontendmenu + mainmenu + settings + optioncatwalkfour pending."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

prefixes = ["frontendmenu", "mainmenu", "settings", "optioncatwalkfour"]
buckets = {p: [] for p in prefixes}

for k, v in strings.items():
    if v.get("status") == "translated":
        continue
    key_l = k.lower()
    for p in prefixes:
        if key_l.startswith(p):
            buckets[p].append({
                "key": k,
                "source": v.get("source", ""),
                "context": v.get("context", ""),
                "max_length": v.get("max_length"),
            })
            break

for p in prefixes:
    print(f"{p}: {len(buckets[p])}")
total = sum(len(v) for v in buckets.values())
print("Toplam:", total)

out = {"items": [item for p in prefixes for item in buckets[p]]}
Path("../translations/batch6_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Yazildi: translations/batch6_source.json")
