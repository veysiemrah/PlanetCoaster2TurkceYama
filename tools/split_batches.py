"""optionsmenu stringlerini 3 batch'e böler."""
import json
from pathlib import Path

data = json.loads(Path("../translations/optionsmenu_source.json").read_text(encoding="utf-8"))
items = list(data.items())
total = len(items)
size = total // 3

b1 = dict(items[:size])
b2 = dict(items[size:2*size])
b3 = dict(items[2*size:])

Path("../translations/optionsmenu_batch1.json").write_text(
    json.dumps(b1, ensure_ascii=False, indent=2), encoding="utf-8")
Path("../translations/optionsmenu_batch2.json").write_text(
    json.dumps(b2, ensure_ascii=False, indent=2), encoding="utf-8")
Path("../translations/optionsmenu_batch3.json").write_text(
    json.dumps(b3, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"B1: {len(b1)}, B2: {len(b2)}, B3: {len(b3)}")
print(f"B1: {list(b1.keys())[0]} -> {list(b1.keys())[-1]}")
print(f"B2: {list(b2.keys())[0]} -> {list(b2.keys())[-1]}")
print(f"B3: {list(b3.keys())[0]} -> {list(b3.keys())[-1]}")
