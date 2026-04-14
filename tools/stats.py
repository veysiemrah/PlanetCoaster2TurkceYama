"""Çeviri istatistiklerini gösterir."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

total = len(strings)
translated = sum(1 for e in strings.values() if e.get("status") == "translated")
pending = total - translated

by_cat = {}
for key, entry in strings.items():
    cat = entry.get("category", "uncategorized")
    status = entry.get("status", "pending")
    if cat not in by_cat:
        by_cat[cat] = {"translated": 0, "pending": 0}
    slot = "translated" if status == "translated" else "pending"
    by_cat[cat][slot] += 1

print(f"=== CEVIRME DURUMU ===")
print(f"Toplam: {total}")
print(f"Cevrildi: {translated} ({translated*100//total}%)")
print(f"Bekliyor: {pending}")
print()
print("Kategori bazinda:")
for cat, counts in sorted(by_cat.items()):
    t = counts["translated"]
    p = counts["pending"]
    total_cat = t + p
    bar = "#" * (t * 20 // total_cat) if total_cat else ""
    print(f"  {cat:<30} {t:>5}/{total_cat:<5} [{bar:<20}]")
