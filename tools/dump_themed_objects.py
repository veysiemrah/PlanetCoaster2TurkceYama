"""Tema nesneleri ve büyük kategoriler için kaynak dosyaları oluşturur."""
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
        print(f"ATLANDI: {prefix}")
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

# Tema nesneleri (tek dosyada birleştir)
dump("pc_", "../translations/pc_source.json")
dump("aq_", "../translations/aq_source.json")
dump("my_", "../translations/my_source.json")
dump("fr_", "../translations/fr_source.json")
dump("re_", "../translations/re_source.json")
dump("vi_", "../translations/vi_source.json")
dump("tk_", "../translations/tk_source.json")

# Büyük kategoriler
dump("buildingpartname_", "../translations/buildingpartname_source.json", n_batches=8)
dump("vo_", "../translations/vo_source.json", n_batches=4)
dump("triggeredaudioevents_", "../translations/triggeredaudioevents_source.json")
dump("stagename_", "../translations/stagename_source.json")

# Guestname - özel isimler, çevrilmeyecek
# guestname_ atlandı

# trackeditparam
dump("trackeditparam_", "../translations/trackeditparam_source.json")
