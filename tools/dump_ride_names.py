"""Tum eglence birimi (flatride/waterslide/coaster/transport/powered) isimlerini dump et.

'_desc' bitenleri atla, sadece ana isimleri al.
"""
import json
import re
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

# Prefix pattern'leri — ride type tematik prefix
RIDE_KEY_RE = re.compile(
    r"^("
    r"[a-z]{2,3}_flatride_[a-z0-9_]+|"
    r"[a-z]{2,3}_coaster_[a-z0-9_]+|"
    r"[a-z]{2,3}_waterride_[a-z0-9_]+|"
    r"[a-z]{2,3}_waterslide_[a-z0-9_]+|"
    r"fr_[a-z0-9_]+|"
    r"water_[a-z0-9_]+|"
    r"transport_[a-z0-9_]+|"
    r"transport_model_[a-z0-9_]+|"
    r"transport_tr_[a-z0-9_]+|"
    r"powered_[a-z0-9_]+|"
    r"fanfarecoaster_[a-z0-9_]+|"
    r"techtreelabel_[a-z0-9_]+"
    r")$"
)

# Exclude desc, category, param, element keys
EXCLUDE = ("_desc", "_prefix", "_context", "_tooltip", "_stat")

rides = []
for k, v in strings.items():
    if not RIDE_KEY_RE.match(k):
        continue
    if any(k.endswith(x) for x in EXCLUDE):
        continue
    src = v.get("source", "").strip()
    trn = v.get("translation", "").strip()
    # Skip format strings and very short
    if "{" in src or len(src) < 3:
        continue
    # Focus on strings that look like ride names (title case, < 80 chars)
    if len(src) > 80:
        continue
    rides.append((k, src, trn))

print(f"Toplam: {len(rides)}")

# Output grouped by source name (to spot inconsistencies)
from collections import defaultdict
by_source = defaultdict(list)
for k, s, t in rides:
    by_source[s].append((k, t))

# Print all
Path("../ride_review.txt").write_text(
    "\n".join(
        f"=== {s} ===\n" + "\n".join(f"  {k:<55} -> {t}" for k, t in sorted(items))
        for s, items in sorted(by_source.items())
    ),
    encoding="utf-8",
)
print("Yazildi: ride_review.txt")
