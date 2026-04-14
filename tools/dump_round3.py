"""3. tur çeviri için kaynak dosyaları oluşturur."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

def dump(prefix, out_path, n_batches=1):
    result = {}
    for key, entry in strings.items():
        if key.startswith(prefix):
            if entry.get("status") != "translated":
                result[key] = entry.get("source", "")
    if not result:
        print(f"ATLANDI: {prefix} (zaten çevrilmiş veya yok)")
        return
    if n_batches == 1:
        Path(out_path).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Yazildi: {out_path} ({len(result)} string)")
    else:
        items = list(result.items())
        size = len(items) // n_batches
        for i in range(n_batches):
            start = i * size
            end = (i + 1) * size if i < n_batches - 1 else len(items)
            batch = dict(items[start:end])
            p = out_path.replace(".json", f"_b{i+1}.json")
            Path(p).write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"Yazildi: {p} ({len(batch)} string)")

dump("tag_", "../translations/tag_source.json")
dump("triggeredaudioevents_", "../translations/triggeredaudioevents_source.json")
dump("objectbrowser_", "../translations/objectbrowser_source.json")
dump("music_", "../translations/music_source.json")
dump("trackelementdesc_", "../translations/trackelementdesc_source.json")
dump("pathedit_", "../translations/pathedit_source.json")
dump("sequence_", "../translations/sequence_source.json")
dump("techtreelabel_", "../translations/techtreelabel_source.json")
dump("parkexpansion_", "../translations/parkexpansion_source.json")
dump("sandboxsettings_", "../translations/sandboxsettings_source.json")
dump("blueprint_", "../translations/blueprint_source.json")
dump("franchise_", "../translations/franchise_source.json")
dump("heatmap_", "../translations/heatmap_source.json")
dump("guests_", "../translations/guests_source.json")
dump("input_", "../translations/input_source.json")
dump("blueprints_", "../translations/blueprints_source.json")
dump("terrain_", "../translations/terrain_source.json")
dump("browser_", "../translations/browser_source.json")
dump("radialmenu_", "../translations/radialmenu_source.json")
dump("semantictag_", "../translations/semantictag_source.json")
dump("shopitem_", "../translations/shopitem_source.json")
