"""Tüm bekleyen _translated.json dosyalarını tr.json'a uygular."""
import json
import sys
from pathlib import Path

tr_json_path = Path("../translations/Content0/tr.json")
data = json.loads(tr_json_path.read_text(encoding="utf-8"))
strings = data["strings"]

# Kategori adı → dosya listesi
pending = [
    ("pathedit", ["../translations/pathedit_translated.json"]),
    ("sequence", ["../translations/sequence_translated.json"]),
    ("terrain", ["../translations/terrain_translated.json"]),
    ("music", ["../translations/music_translated.json"]),
    ("browser", ["../translations/browser_translated.json"]),
    ("guests", ["../translations/guests_translated.json"]),
    ("radialmenu", ["../translations/radialmenu_translated.json"]),
    ("input", ["../translations/input_translated.json"]),
    ("semantictag", ["../translations/semantictag_translated.json"]),
    ("trackelementdesc", ["../translations/trackelementdesc_translated.json"]),
    ("shopitem", ["../translations/shopitem_translated.json"]),
    ("blueprint", ["../translations/blueprint_translated.json"]),
    ("franchise", ["../translations/franchise_translated.json"]),
    ("heatmap", ["../translations/heatmap_translated.json"]),
    ("sandboxsettings", ["../translations/sandboxsettings_translated.json"]),
    ("parkexpansion", ["../translations/parkexpansion_translated.json"]),
]

total_updated = 0
for category, files in pending:
    cat_updated = 0
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
                cat_updated += 1
        print(f"  {p.name}: {cat_updated} string")
    total_updated += cat_updated

tr_json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nToplam guncellendi: {total_updated} string")
