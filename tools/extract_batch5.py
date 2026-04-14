"""Batch 5."""
import json
from pathlib import Path

PREFIXES = ["frontieraccountsignup", "cameraoptionsmenu", "loadingscreen", "colourgrading", "guestmood"]

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

out = {}
for prefix in PREFIXES:
    batch = {}
    for k, v in strings.items():
        if not k.startswith(prefix):
            continue
        if v.get("status") == "translated":
            continue
        batch[k] = v["source"]
    out[prefix] = batch
    print(f"{prefix:<25} {len(batch):>4}")

total = sum(len(b) for b in out.values())
print(f"{'TOPLAM':<25} {total:>4}")

Path("../translations/batch5_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
