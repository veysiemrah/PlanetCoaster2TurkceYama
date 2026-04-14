"""Birden fazla kategoriyi batch JSON dosyalarına çıkarır."""
import json
from pathlib import Path
import sys

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

def dump(prefix, out_path, n_batches=1):
    result = {}
    for key, entry in strings.items():
        if key.startswith(prefix):
            result[key] = entry.get("source", "")

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

dump("graphicsoptionsmenu_", "../translations/graphicsoptionsmenu_source.json")
dump("notification_", "../translations/notification_source.json")
dump("guest_thought", "../translations/guest_thought_source.json", n_batches=3)
dump("parkmanagement_", "../translations/parkmanagement_source.json", n_batches=3)
