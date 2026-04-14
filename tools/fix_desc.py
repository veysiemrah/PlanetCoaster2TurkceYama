import json
from pathlib import Path

p = Path("../translations/Content0/tr.json")
data = json.loads(p.read_text(encoding="utf-8"))
strings = data["strings"]

FIXES = {
    "re_flatride_boardslide_desc": "Resort temalı Boardslide eğlencesi.",
    "re_flatride_forge_desc": "Resort temalı Forge eğlencesi.",
    "re_flatride_monsoonchute_desc": "Resort temalı Monsoon Chute eğlencesi.",
    "re_flatride_polarity_desc": "Resort temalı Polarity eğlencesi.",
    "re_flatride_tinyeye_desc": "Resort temalı Tiny Eye eğlencesi.",
    "vi_flatride_mecharoller_desc": "Viking temalı Mecha Roller eğlencesi.",
    "vi_flatride_upswing_desc": "Viking temalı Upswing eğlencesi.",
}

n = 0
for k, v in FIXES.items():
    if k in strings:
        strings[k]["translation"] = v
        n += 1

p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Uygulanan: {n}")
