"""tr.json'daki tüm key prefix'lerini ve sayılarını listeler."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

prefixes = {}
for key in strings:
    prefix = key.split("_")[0]
    prefixes[prefix] = prefixes.get(prefix, 0) + 1

for prefix, count in sorted(prefixes.items(), key=lambda x: -x[1]):
    status_translated = sum(1 for k, e in strings.items() if k.startswith(prefix + "_") and e.get("status") == "translated")
    status_translated += sum(1 for k, e in strings.items() if k == prefix and e.get("status") == "translated")
    print(f"{prefix:<30} {count:>5}  (cevirildi: {status_translated})")
