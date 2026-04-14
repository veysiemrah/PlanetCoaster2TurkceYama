"""Flat Ride 4. pass - son kalan varyantlar"""
import json, shutil

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review6d'
shutil.copy2(SRC, BAK)

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

REPLACEMENTS = [
    # "Düz Eğlenceler" / "düz eğlenceler" (birimsiz plural)
    ('Düz Eğlencelerin', 'Sabit Oyunların'),
    ('Düz Eğlenceler', 'Sabit Oyunlar'),
    ('düz eğlencelerin', 'sabit oyunların'),
    ('düz eğlencelere', 'sabit oyunlara'),
    ('düz eğlenceleri', 'sabit oyunları'),
    ('düz eğlenceler', 'sabit oyunlar'),
    # "düz eğlence" / "Düz Eğlence" (singular, birimsiz)
    ('Düz Eğlencenin', 'Sabit Oyunun'),
    ('Düz Eğlence', 'Sabit Oyun'),
    ('düz eğlencenin', 'sabit oyunun'),
    ('düz eğlencesinin', 'sabit oyunun'),
    ('düz eğlencenin', 'sabit oyunun'),
    ('düz eğlence', 'sabit oyun'),
    # "sabit eğlence" lowercase birimsiz kalanlar
    ('sabit eğlencenin', 'sabit oyunun'),
    ('sabit eğlence', 'sabit oyun'),
    # "Düz atraksiyon" lowercase
    ('Düz atraksiyonlarının', 'Sabit Oyunlarının'),
    ('Düz atraksiyonları', 'Sabit Oyunları'),
    ('Düz atraksiyon', 'Sabit Oyun'),
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
        changes.append((k, tr, new_tr))

# "Sürüş Fiyatı" bir özel durum (parkmanagement_flatride_price)
if 'parkmanagement_flatride_price' in strings:
    e = strings['parkmanagement_flatride_price']
    if e['translation'] == 'Sürüş Fiyatı':
        e['translation'] = 'Sabit Oyun Fiyatı'
        changes.append(('parkmanagement_flatride_price', 'Sürüş Fiyatı', 'Sabit Oyun Fiyatı'))

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'{len(changes)} kayıt değişti.')
for k, old, new in changes:
    print(f'\n[{k}]\n  Ö: {old[:120]}\n  S: {new[:120]}')
