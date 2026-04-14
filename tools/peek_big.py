"""buildingpartname ve vo önizlemesi."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

for prefix in ["buildingpartname", "vo", "triggeredaudioevents", "stagename"]:
    keys = [k for k in strings if k.startswith(prefix + "_")]
    print(f"\n--- {prefix}_ ({len(keys)} key) ---")
    for k in keys[:5]:
        src = strings[k].get("source", "")[:80]
        print(f"  {k}: {repr(src)}")
