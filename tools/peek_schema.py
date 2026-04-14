"""Kayit semasini incele."""
import json
from pathlib import Path

d = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = d["strings"]

# Ilk 2 kayit
for k, v in list(strings.items())[:2]:
    print(k)
    for field, val in v.items():
        s = str(val)[:80]
        print(f"  {field}: {s}")
    print()

# Ilk guestname
print("--- guestname ornek ---")
for k, v in strings.items():
    if k.startswith("guestname"):
        print(k)
        for field, val in v.items():
            s = str(val)[:80]
            print(f"  {field}: {s}")
        break

# Cevrilmis bir ornek (karsilastirma icin)
print("\n--- cevrilmis ornek ---")
for k, v in strings.items():
    if v.get("status") == "translated":
        print(k)
        for field, val in v.items():
            s = str(val)[:80]
            print(f"  {field}: {s}")
        break
