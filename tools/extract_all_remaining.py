"""Kalan tum pending (uncategorized) string'leri tek dosyaya cikar."""
import json
from pathlib import Path

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
strings = data["strings"]

pending = []
for k, v in strings.items():
    if v.get("status") == "translated":
        continue
    pending.append({
        "key": k,
        "source": v.get("source", ""),
        "context": v.get("context", ""),
        "max_length": v.get("max_length"),
    })

print(f"Toplam pending: {len(pending)}")

out = {"items": pending}
Path("../translations/batch17_source.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Yazildi: translations/batch17_source.json")
