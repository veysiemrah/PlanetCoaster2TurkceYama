"""Her dosyada kac eglence birimi var ve kac cekici kaldi sayar"""
import re, json, sys
from pathlib import Path

sc = '\u00e7'
bc = '\u00c7'

# cekicilik ve turevleri haric (k->g yumusmasi dahil)
CEKICI_PATTERN = re.compile(
    r'[' + re.escape(bc + sc) + r']ekici(?!li[k\u011f]\w*|lik\w*)',
    re.UNICODE
)
EGLENCE_PATTERN = re.compile(r'e\u011flence birimi', re.IGNORECASE)

files = sys.argv[1:] if len(sys.argv) > 1 else []

total_cekici = 0
total_eglence = 0

for filepath in files:
    path = Path(filepath)
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    cekici = 0
    eglence = 0
    for val in data.values():
        if isinstance(val, str):
            cekici += len(CEKICI_PATTERN.findall(val))
            eglence += len(EGLENCE_PATTERN.findall(val))

    total_cekici += cekici
    total_eglence += eglence
    status = "OK" if cekici == 0 else "KALAN VAR!"
    print(f"[{status}] {path.name}: cekici_kalan={cekici}, eglence_birimi={eglence}")

print()
print(f"TOPLAM: cekici_kalan={total_cekici}, eglence_birimi={total_eglence}")
