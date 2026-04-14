"""Sonraki çeviri turları için kaynak dosyalarını oluşturur."""
import json
from pathlib import Path
import sys

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

def dump(prefix, out_path, n_batches=1):
    result = {}
    for key, entry in strings.items():
        if key.startswith(prefix):
            if entry.get("status") != "translated":  # sadece çevrilmemişleri al
                result[key] = entry.get("source", "")

    if not result:
        print(f"ATLANDI: {prefix} (zaten tümü çevrilmiş)")
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
            print(f"Yazildi: {p} ({len(batch)} string, {list(batch.keys())[0]} -> {list(batch.keys())[-1]})")

# Sonraki tur çeviriler
dump("infopanel_", "../translations/infopanel_source.json", n_batches=5)
dump("frontend_", "../translations/frontend_source.json", n_batches=2)
dump("objective_", "../translations/objective_source.json", n_batches=2)
dump("trackelementname_", "../translations/trackelementname_source.json", n_batches=2)
dump("objectives_", "../translations/objectives_source.json", n_batches=2)
dump("tutorialscreen_", "../translations/tutorialscreen_source.json", n_batches=2)
dump("coaster_", "../translations/coaster_source.json")
dump("workshop_", "../translations/workshop_source.json")
dump("shopitem_", "../translations/shopitem_source.json")
dump("staff_", "../translations/staff_source.json")
