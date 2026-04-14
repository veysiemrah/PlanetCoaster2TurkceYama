"""Mevcut çeviri durumunu gösterir ve batch dosyalarını kontrol eder."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]
cats = {}
for k, v in strings.items():
    cat = v.get("category", "unknown")
    if cat not in cats:
        cats[cat] = {"total": 0, "translated": 0}
    cats[cat]["total"] += 1
    if v.get("status") == "translated":
        cats[cat]["translated"] += 1

print(f"Toplam: {len(strings)} string")
print()
for cat, c in sorted(cats.items(), key=lambda x: -x[1]["translated"]):
    if c["translated"] > 0:
        print(f"{cat}: {c['translated']}/{c['total']}")
