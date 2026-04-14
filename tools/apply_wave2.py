"""2. dalga çevirilerini tr.json'a uygular."""
import json
from pathlib import Path

tr_json_path = Path("../translations/Content0/tr.json")
data = json.loads(tr_json_path.read_text(encoding="utf-8"))
strings = data["strings"]

pending = [
    # Tema nesneleri
    ("pc", ["../translations/pc_translated.json"]),
    ("aq", ["../translations/aq_translated.json"]),
    ("my", ["../translations/my_translated.json"]),
    ("fr", ["../translations/fr_translated.json"]),
    ("re", ["../translations/re_translated.json"]),
    ("vi", ["../translations/vi_translated.json"]),
    ("tk", ["../translations/tk_translated.json"]),
    # buildingpartname (8 batch)
    ("buildingpartname", [
        "../translations/buildingpartname_translated_b1.json",
        "../translations/buildingpartname_translated_b2.json",
        "../translations/buildingpartname_translated_b3.json",
        "../translations/buildingpartname_translated_b4.json",
        "../translations/buildingpartname_translated_b5.json",
        "../translations/buildingpartname_translated_b6.json",
        "../translations/buildingpartname_translated_b7.json",
        "../translations/buildingpartname_translated_b8.json",
    ]),
    # vo (4 batch)
    ("vo", [
        "../translations/vo_translated_b1.json",
        "../translations/vo_translated_b2.json",
        "../translations/vo_translated_b3.json",
        "../translations/vo_translated_b4.json",
    ]),
    # Küçük kategoriler
    ("triggeredaudioevents", ["../translations/triggeredaudioevents_translated.json"]),
    ("stagename", ["../translations/stagename_translated.json"]),
    ("trackeditparam", ["../translations/trackeditparam_translated.json"]),
]

total = 0
for category, files in pending:
    cat_count = 0
    for fpath in files:
        p = Path(fpath)
        if not p.exists():
            print(f"ATLA (yok): {fpath}")
            continue
        try:
            translations = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            translations = json.loads(p.read_text(encoding="utf-8-sig"))
        for key, translation in translations.items():
            if key in strings and translation:
                strings[key]["translation"] = translation
                strings[key]["status"] = "translated"
                strings[key]["category"] = category
                cat_count += 1
    if cat_count:
        print(f"{category}: {cat_count} string")
    total += cat_count

tr_json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nToplam guncellendi: {total} string")
