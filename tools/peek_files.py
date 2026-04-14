import json
from pathlib import Path

files = ["tag", "triggeredaudioevents", "music", "guests", "input", "semantictag", "objectbrowser", "pathedit"]
for f in files:
    p = Path(f"../translations/{f}_source.json")
    if not p.exists():
        continue
    data = json.loads(p.read_text(encoding="utf-8"))
    items = list(data.items())[:3]
    print(f"--- {f} ({len(data)}) ---")
    for k, v in items:
        print(f"  {k}: {repr(v[:70])}")
