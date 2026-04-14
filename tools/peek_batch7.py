import json
from pathlib import Path

data = json.loads(Path("../translations/batch7_source.json").read_text(encoding="utf-8"))

for prefix in ["pathresource", "toolpanelfoliagescenery"]:
    print(f"=== {prefix} ===")
    for item in data["items"]:
        if item["key"].startswith(prefix):
            src = item["source"][:80].replace("\n", " ")
            print(f"  {item['key']:<55} | {src}")
    print()
