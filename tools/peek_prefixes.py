"""2 harfli prefix'lerin içeriğini gösterir."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

short_prefixes = ["pc", "aq", "my", "fr", "re", "vi", "tk"]

for prefix in short_prefixes:
    keys = [k for k in strings if k.startswith(prefix + "_")]
    print(f"\n--- {prefix}_ ({len(keys)} key) ---")
    for k in keys[:4]:
        src = strings[k].get("source", "")[:70]
        print(f"  {k}: {repr(src)}")
