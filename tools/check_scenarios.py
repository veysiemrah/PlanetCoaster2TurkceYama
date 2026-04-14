"""Kariyer senaryo baslıklarının mevcut Turkce cevirilerini bul."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

scenarios = [
    "Paradise Lost", "Building the Bifröst", "Coaster Chasm",
    "A Shore Thing", "Double Trouble", "Just The Thicket",
    "The Garden of Edith", "Junkyard Park", "Labyrinth Secrets",
    "Lazy River Styx", "Parks and Restoration", "Mascot Madness",
    "Fabled Fjord", "Pest Problem", "Farmland Fiasco",
    "Private Park", "The Brothers Swimm", "Swamp Scenario",
    "Sky's The Limit", "Keys to the Coaster", "In The Swim of Things",
    "Summit Awesome", "Thrills'n'Spills",
]

for scenario in scenarios:
    found_in = []
    for k, v in strings.items():
        if v.get("status") != "translated":
            continue
        if scenario in v.get("source", ""):
            key_short = k[:60]
            trn = v.get("translation", "")[:80].replace("\n", " ")
            found_in.append((key_short, trn))
            if len(found_in) >= 2:
                break
    if found_in:
        print(f"\n=== {scenario} ===")
        for k, t in found_in:
            print(f"  {k}: {t}")
    else:
        print(f"BULUNAMADI: {scenario}")
