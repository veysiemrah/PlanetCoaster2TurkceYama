import json
from pathlib import Path
from collections import Counter

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
cats = Counter()
for entry in data["strings"].values():
    cats[entry.get("category", "(bos)")] += 1
for cat, n in cats.most_common(40):
    print(f"{n:6}  {cat}")
