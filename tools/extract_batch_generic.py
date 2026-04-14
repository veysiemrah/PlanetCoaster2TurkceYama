"""Generic batch extractor. Kullanim:
python extract_batch_generic.py <batch_no> <prefix1> <prefix2> ...

Prefix sonuna '_' koymaya gerek yok, otomatik eklenir.
"""
import json
import sys
from pathlib import Path

if len(sys.argv) < 3:
    sys.exit("Kullanim: python extract_batch_generic.py <batch_no> <prefix1> [<prefix2> ...]")

n = sys.argv[1]
raw_prefixes = sys.argv[2:]

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

# Sirali set - daha uzun prefix'ler once degerlendirilsin
exact_prefixes = sorted(
    [(p + "_" if not p.endswith("_") else p, p.rstrip("_")) for p in raw_prefixes],
    key=lambda x: -len(x[0]),
)

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
total = sum(len(v) for v in buckets.values())
print(f"Toplam: {total}")

out = {"items": [item for cat in buckets for item in buckets[cat]]}
Path(f"../translations/batch{n}_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(f"Yazildi: translations/batch{n}_source.json")
