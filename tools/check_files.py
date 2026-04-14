"""Batch dosyalarının durumunu kontrol eder - source mi translation mi?"""
import json
from pathlib import Path

files = [
    "../translations/graphicsoptionsmenu_source.json",
    "../translations/notification_source.json",
    "../translations/guest_thought_source_b1.json",
    "../translations/guest_thought_source_b2.json",
    "../translations/guest_thought_source_b3.json",
]

# Load tr.json to compare
tr_data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
tr_strings = tr_data["strings"]

for fpath in files:
    p = Path(fpath)
    if not p.exists():
        print(f"BULUNAMADI: {fpath}")
        continue
    data = json.loads(p.read_text(encoding="utf-8"))
    keys = list(data.keys())
    # Check first value - if it's Turkish (contains Turkish chars or different from tr.json source)
    first_key = keys[0]
    first_val = data[first_key]
    source_val = tr_strings.get(first_key, {}).get("source", "")
    is_translated = (first_val != source_val) and len(first_val) > 0
    print(f"\n{p.name}: {len(data)} keys")
    print(f"  First key: {first_key}")
    print(f"  File value: {repr(first_val[:80])}")
    print(f"  Source val: {repr(source_val[:80])}")
    print(f"  Is translated: {is_translated}")
