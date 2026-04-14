"""guest_thought batch 2 dosyasını kontrol eder."""
import json
from pathlib import Path

b2 = json.loads(Path("../translations/guest_thought_source_b2.json").read_text(encoding="utf-8"))
items = list(b2.items())
print(f"B2 toplam: {len(items)} key")
print("Ilk 3:")
for k, v in items[:3]:
    print(f"  {k}: {repr(v[:100])}")
print("...")
print("Son 3:")
for k, v in items[-3:]:
    print(f"  {k}: {repr(v[:100])}")
