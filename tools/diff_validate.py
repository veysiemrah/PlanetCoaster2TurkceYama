"""Batch N prefix'lerinde glossary uyarilari."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import check_glossary, load_glossary

PREFIXES = sys.argv[1:] if len(sys.argv) > 1 else ["chapter"]

data = json.loads(Path("../translations/Content0/tr.json").read_text(encoding="utf-8"))
glossary = load_glossary(Path("../glossary.json"))

issues = []
for key, entry in data["strings"].items():
    if not any(key.startswith(p) for p in PREFIXES):
        continue
    warnings = check_glossary(key, entry["source"], entry["translation"], glossary)
    for w in warnings:
        issues.append(w)

print(f"Uyari: {len(issues)}")
for w in issues[:30]:
    print(f"  {w}")
