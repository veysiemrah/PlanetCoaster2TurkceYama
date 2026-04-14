"""istasyon -> Istasyon duzelt."""
import json
from pathlib import Path

p = Path("../translations/batch2_translated.json")
data = json.loads(p.read_text(encoding="utf-8"))
st = data["station"]
changed = 0
for k, v in st.items():
    new = v.replace("istasyon", "İstasyon")
    if new != v:
        st[k] = new
        changed += 1
p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Guncellenen: {changed}")
