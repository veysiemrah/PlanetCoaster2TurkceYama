"""Belirli bir kategorideki stringleri key: source formatında döker."""
import json
import sys
from pathlib import Path

prefix = sys.argv[1] if len(sys.argv) > 1 else "optionsmenu_"
out_file = sys.argv[2] if len(sys.argv) > 2 else None

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

result = {}
for key, entry in strings.items():
    if key.startswith(prefix):
        result[key] = entry.get("source", "")

if out_file:
    import json as j
    Path(out_file).write_text(j.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Yazildi: {out_file} ({len(result)} string)")
else:
    for key, src in result.items():
        print(f'"{key}": "{src}",')
    print(f"\n# Toplam: {len(result)}")
