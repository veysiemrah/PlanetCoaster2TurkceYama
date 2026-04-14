import json
from pathlib import Path

data = json.loads(Path("../translations/popup_source.json").read_text(encoding="utf-8"))
items = list(data.items())
total = len(items)
size = total // 3

b1 = dict(items[:size])
b2 = dict(items[size:2*size])
b3 = dict(items[2*size:])

Path("../translations/popup_batch1.json").write_text(json.dumps(b1, ensure_ascii=False, indent=2), encoding="utf-8")
Path("../translations/popup_batch2.json").write_text(json.dumps(b2, ensure_ascii=False, indent=2), encoding="utf-8")
Path("../translations/popup_batch3.json").write_text(json.dumps(b3, ensure_ascii=False, indent=2), encoding="utf-8")

print("B1:", len(b1), list(b1.keys())[0], "->", list(b1.keys())[-1])
print("B2:", len(b2), list(b2.keys())[0], "->", list(b2.keys())[-1])
print("B3:", len(b3), list(b3.keys())[0], "->", list(b3.keys())[-1])
