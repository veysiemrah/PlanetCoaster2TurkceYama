"""Uncategorized pending string'leri incele."""
import json
from collections import Counter
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

uncat = [(k, v) for k, v in strings.items()
         if not v.get("category")
         and v.get("status") != "translated"]

print(f"Toplam uncategorized pending: {len(uncat)}")
print()

# Prefix'lere gore grup
prefixes = Counter()
for k, _ in uncat:
    # key formati genelde "Category/Section/name" veya "CategoryName"
    if "/" in k:
        pre = k.split("/")[0]
    elif "_" in k:
        pre = k.split("_")[0]
    else:
        pre = k[:20]
    prefixes[pre] += 1

print("En yaygin 25 prefix:")
for pre, cnt in prefixes.most_common(25):
    print(f"  {cnt:>5}  {pre}")

print()
print("Ilk 20 ornek:")
for k, v in uncat[:20]:
    src = v.get("source_text", v.get("source", ""))
    src = src[:80].replace("\n", " ")
    print(f"  {k[:60]:<60} | {src}")
