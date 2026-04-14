"""Content0 içindeki menü/UI string'lerini bulur."""
import json
from pathlib import Path
from collections import Counter

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

# Key prefix'lerine göre grupla
prefixes = Counter()
for key in strings:
    prefix = key.split("_")[0] if "_" in key else key
    prefixes[prefix] += 1

print("=== KEY PREFIX DAĞILIMI (ilk 40) ===")
for p, n in prefixes.most_common(40):
    print(f"{n:6}  {p}")

# Menü ile ilgili olabilecek key'leri ara
print("\n=== MENU/UI İLE İLGİLİ KEY'LER (ilk 50) ===")
menu_keywords = ["menu", "ui", "button", "screen", "panel", "tab", "tooltip",
                 "title", "label", "hud", "popup", "dialog", "notification", "main"]
count = 0
for key, entry in strings.items():
    if any(kw in key.lower() for kw in menu_keywords):
        src = entry["source"][:70]
        print(f"  {key[:50]}: {src}")
        count += 1
        if count >= 50:
            break
