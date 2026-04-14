"""Credits icerisindeki unique role adlarini cikar."""
import json
import re
from pathlib import Path

data = json.loads(Path("../translations/batch7_source.json").read_text(encoding="utf-8"))

h1_set = set()
h2_set = set()

H1_RE = re.compile(r"<h1>([^<]+)</h1>")
H2_RE = re.compile(r"<h2>([^<]+)</h2>")

for item in data["items"]:
    if not item["key"].startswith("credits"):
        continue
    for m in H1_RE.findall(item["source"]):
        h1_set.add(m.strip())
    for m in H2_RE.findall(item["source"]):
        h2_set.add(m.strip())

print(f"Unique h1: {len(h1_set)}")
for v in sorted(h1_set):
    print(f"  {v}")

print(f"\nUnique h2: {len(h2_set)}")
for v in sorted(h2_set):
    print(f"  {v}")
