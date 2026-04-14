import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

pending = [(k, v) for k, v in strings.items()
           if v.get("status") != "translated" and not v.get("category")]
print("Total pending uncategorized:", len(pending))

if pending:
    k, v = pending[0]
    print("Sample keys:", list(v.keys()))
    print("Sample record:", v)
