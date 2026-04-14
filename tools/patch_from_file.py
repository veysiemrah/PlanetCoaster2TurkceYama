"""Bir çeviri JSON dosyasından tr.json'a çevirileri uygular.

Kullanım:
  python patch_from_file.py <kaynak_dosya> <kategori>

Örnek:
  python patch_from_file.py ../translations/guest_thought_source_b2.json guest_thought
"""
import json
import sys
from pathlib import Path

if len(sys.argv) < 3:
    print("Kullanım: python patch_from_file.py <kaynak_dosya> <kategori>")
    sys.exit(1)

source_path = Path(sys.argv[1])
category = sys.argv[2]

translations = json.loads(source_path.read_text(encoding="utf-8"))

tr_json_path = Path("../translations/Content0/tr.json")
data = json.loads(tr_json_path.read_text(encoding="utf-8"))
strings = data["strings"]

updated = 0
not_found = 0
for key, translation in translations.items():
    if key in strings:
        strings[key]["translation"] = translation
        strings[key]["status"] = "translated"
        strings[key]["category"] = category
        updated += 1
    else:
        not_found += 1
        if not_found <= 5:
            print(f"  BULUNAMADI: {key}")

tr_json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"{updated} string guncellendi, {not_found} bulunamadi.")
