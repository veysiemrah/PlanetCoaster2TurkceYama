"""guestname alt kategorilerini say."""
import json
from collections import Counter
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
c = Counter()
for k in data["strings"]:
    if k.startswith("guestname_forename_female"):
        c["forename_female"] += 1
    elif k.startswith("guestname_forename_male"):
        c["forename_male"] += 1
    elif k.startswith("guestname_surname"):
        c["surname"] += 1
    elif k.startswith("guestname_default"):
        c["default"] += 1
    elif k.startswith("guestname"):
        c["other"] += 1

for k, v in sorted(c.items()):
    print(f"  {k:<20} {v:>5}")
print(f"  {'TOPLAM':<20} {sum(c.values()):>5}")
