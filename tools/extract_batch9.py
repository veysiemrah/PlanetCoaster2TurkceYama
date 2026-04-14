"""Batch 9: keplerrequesterror + trackelementdisabled + set + challenge pending.

NOT: 'set' ve 'challenge' prefix'leri daha uzun prefix'lerle (settings_, challenges_)
karismamasi icin oncelik sirasi onemli. Exact underscore ile ayirt et.
"""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

# Sira onemli: daha uzun/spesifik prefix'ler once
EXCLUDE_PREFIXES = ["settings_", "challenges_"]
EXACT_PREFIXES = [
    ("keplerrequesterror_", "keplerrequesterror"),
    ("trackelementdisabled_", "trackelementdisabled"),
    ("set_", "set"),
    ("challenge_", "challenge"),
]
buckets = {cat: [] for _, cat in EXACT_PREFIXES}

for k, v in strings.items():
    if v.get("status") == "translated":
        continue
    key_l = k.lower()
    if any(key_l.startswith(ex) for ex in EXCLUDE_PREFIXES):
        continue
    for pre, cat in EXACT_PREFIXES:
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
Path("../translations/batch9_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Yazildi: translations/batch9_source.json")
