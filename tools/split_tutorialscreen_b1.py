"""tutorialscreen_source_b1.json'u 2 alt batch'e böler."""
import json
from pathlib import Path

data = json.loads(Path("../translations/tutorialscreen_source_b1.json").read_text(encoding="utf-8"))
items = list(data.items())
mid = len(items) // 2

b1a = dict(items[:mid])
b1b = dict(items[mid:])

Path("../translations/tutorialscreen_source_b1a.json").write_text(
    json.dumps(b1a, ensure_ascii=False, indent=2), encoding="utf-8"
)
Path("../translations/tutorialscreen_source_b1b.json").write_text(
    json.dumps(b1b, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(f"b1a: {len(b1a)} string, b1b: {len(b1b)} string")
