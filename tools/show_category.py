"""Belirli bir key prefix'ine sahip string'leri listeler."""
import json
import sys
from pathlib import Path

prefix = sys.argv[1] if len(sys.argv) > 1 else "frontendmenu"
data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

count = 0
for key, entry in strings.items():
    if key.startswith(prefix):
        print(f"{key}")
        print(f"  EN: {entry['source']}")
        print()
        count += 1

print(f"Toplam: {count} string")
