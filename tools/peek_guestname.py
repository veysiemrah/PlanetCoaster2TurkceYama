"""guestname prefix'indeki string'leri incele."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

guest = [(k, v) for k, v in strings.items()
         if k.startswith("guestname") and v.get("status") != "translated"]

print(f"Toplam guestname pending: {len(guest)}")
print()
print("Ilk 40 ornek:")
for k, v in guest[:40]:
    src = v.get("source_text", v.get("source", ""))[:60]
    print(f"  {k[:45]:<45} | {src}")

print()
print("Son 10 ornek:")
for k, v in guest[-10:]:
    src = v.get("source_text", v.get("source", ""))[:60]
    print(f"  {k[:45]:<45} | {src}")

# Kac tanesi tek kelime?
single = sum(1 for _, v in guest if len((v.get("source_text") or v.get("source") or "").split()) == 1)
print(f"\nTek kelimelik: {single}/{len(guest)}")
