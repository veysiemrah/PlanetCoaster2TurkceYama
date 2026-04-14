"""Flat Ride 2. pass - ek varyantlar:
  - lowercase 'sabit eğlence birim*'
  - 'Düz Biniş(ler)' / 'düz biniş(ler)'
  - 'Sabit Eğlenceler' / 'sabit eğlenceler' (Birim'siz)
  - 'sabit eğlence' (birimsiz, ride name sentences)
  - 'Eğlence Birimi Paketi' gibi özel ifadeler (case by case)
"""
import json, shutil, re

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review6b'
shutil.copy2(SRC, BAK)

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

# Uzun varyantlar önce
REPLACEMENTS = [
    # Lowercase 'sabit eğlence birim*' (declension destekli)
    ('sabit eğlence birimlerinin', 'sabit oyunların'),
    ('sabit eğlence birimlerine', 'sabit oyunlara'),
    ('sabit eğlence birimlerini', 'sabit oyunları'),
    ('sabit eğlence birimleri', 'sabit oyunlar'),
    ('sabit eğlence biriminin', 'sabit oyunun'),
    ('sabit eğlence birimine', 'sabit oyuna'),
    ('sabit eğlence birimini', 'sabit oyunu'),
    ('sabit eğlence birimi', 'sabit oyun'),
    # 'Düz Biniş(ler)'
    ('Düz Binişler', 'Sabit Oyunlar'),
    ('Düz Biniş', 'Sabit Oyun'),
    ('düz binişler', 'sabit oyunlar'),
    ('düz biniş', 'sabit oyun'),
    # 'Sabit Eğlenceler' (birimsiz)
    ('Sabit Eğlenceler', 'Sabit Oyunlar'),
    ('sabit eğlenceler', 'sabit oyunlar'),
    # Yerel/ispat: "klasik sabit eğlence Pathos III'ü" → "klasik sabit oyun Pathos III'ü"
    # "sabit eğlence Scizzer" → "sabit oyun Scizzer"
    # "Coriolis sabit eğlenceü" (typo) → "Coriolis sabit oyunu"
    ('Coriolis sabit eğlenceü', 'Coriolis sabit oyunu'),
    ('sabit eğlence Pathos', 'sabit oyun Pathos'),
    ('sabit eğlence Scizzer', 'sabit oyun Scizzer'),
    # 'Eğlence Birimi Paketi' (DLC adı, flat ride paketi bağlamında)
    ('Eğlence Birimi Paketi', 'Oyun Paketi'),  # Thrill-Seekers Ride Pack -> Heyecan Arayanlar Oyun Paketi
]

changes = []
for k, v in strings.items():
    tr = v.get('translation', '')
    if not tr:
        continue
    new_tr = tr
    for old, new in REPLACEMENTS:
        new_tr = new_tr.replace(old, new)
    if new_tr != tr:
        strings[k]['translation'] = new_tr
        changes.append((k, tr[:80], new_tr[:80]))

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'{len(changes)} kayıt güncellendi.')
for k, old, new in changes:
    print(f'\n[{k}]\n  Ö: {old}\n  S: {new}')
