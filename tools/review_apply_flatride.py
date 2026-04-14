"""Flat Ride terimini birleştir: hepsi -> "Sabit Oyun"
  - "Düz Oyun*" -> "Sabit Oyun*"
  - "Sabit Eğlence Birim*" -> "Sabit Oyun*"
"""
import json, shutil

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review6'
shutil.copy2(SRC, BAK)

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

# Uzun pattern'ler önce, kısa sonra
REPLACEMENTS = [
    # Sabit Eğlence Birimi (varyantlar, uzun -> kısa)
    ('Sabit Eğlence Birimlerinin', 'Sabit Oyunların'),
    ('Sabit Eğlence Birimlerine', 'Sabit Oyunlara'),
    ('Sabit Eğlence Birimlerini', 'Sabit Oyunları'),
    ('Sabit Eğlence Birimlerinde', 'Sabit Oyunlarda'),
    ('Sabit Eğlence Birimleri', 'Sabit Oyunlar'),
    ('Sabit Eğlence Biriminin', 'Sabit Oyunun'),
    ('Sabit Eğlence Birimine', 'Sabit Oyuna'),
    ('Sabit Eğlence Birimini', 'Sabit Oyunu'),
    ('Sabit Eğlence Biriminde', 'Sabit Oyunda'),
    ("Sabit Eğlence Birimi'nin", "Sabit Oyun'un"),
    ("Sabit Eğlence Birimi'ne", "Sabit Oyun'a"),
    ('Sabit Eğlence Birimi', 'Sabit Oyun'),
    # Düz Oyun (varyantlar)
    ('Düz Oyunların', 'Sabit Oyunların'),
    ('Düz Oyunlara', 'Sabit Oyunlara'),
    ('Düz Oyunları', 'Sabit Oyunları'),
    ('Düz Oyunlar', 'Sabit Oyunlar'),
    ('Düz Oyunun', 'Sabit Oyunun'),
    ('Düz Oyuna', 'Sabit Oyuna'),
    ('Düz Oyunu', 'Sabit Oyunu'),
    ('Düz Oyunda', 'Sabit Oyunda'),
    ('Düz Oyun', 'Sabit Oyun'),
    # Lowercase
    ('düz oyunların', 'sabit oyunların'),
    ('düz oyunlara', 'sabit oyunlara'),
    ('düz oyunları', 'sabit oyunları'),
    ('düz oyunlar', 'sabit oyunlar'),
    ('düz oyunun', 'sabit oyunun'),
    ('düz oyunu', 'sabit oyunu'),
    ('düz oyun', 'sabit oyun'),
]

changed_keys = []
for key, entry in strings.items():
    tr = entry.get('translation', '')
    if not tr:
        continue
    new_tr = tr
    for old, new in REPLACEMENTS:
        new_tr = new_tr.replace(old, new)
    if new_tr != tr:
        strings[key]['translation'] = new_tr
        changed_keys.append(key)

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'{len(changed_keys)} kayıt değişti. Yedek: {BAK}')
for k in changed_keys[:15]:
    print(f'  {k}')
if len(changed_keys) > 15:
    print(f'  ... ve {len(changed_keys) - 15} adet daha')
