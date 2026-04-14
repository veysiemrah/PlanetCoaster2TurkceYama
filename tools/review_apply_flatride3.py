"""Flat Ride 3. pass - tüm kalan varyantlar"""
import json, shutil

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review6c'
shutil.copy2(SRC, BAK)

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

# Uzun -> kısa, ünlü uyumu dahil
REPLACEMENTS = [
    # "Düz Eğlence Birimi" (tüm çekimler)
    ('Düz Eğlence Birimlerinin', 'Sabit Oyunların'),
    ('Düz Eğlence Birimlerine', 'Sabit Oyunlara'),
    ('Düz Eğlence Birimlerini', 'Sabit Oyunları'),
    ('Düz Eğlence Birimleri', 'Sabit Oyunlar'),
    ('Düz Eğlence Biriminin', 'Sabit Oyunun'),
    ('Düz Eğlence Birimine', 'Sabit Oyuna'),
    ('Düz Eğlence Birimini', 'Sabit Oyunu'),
    ('Düz Eğlence Birimi', 'Sabit Oyun'),
    ('düz eğlence birimlerinin', 'sabit oyunların'),
    ('düz eğlence birimlerine', 'sabit oyunlara'),
    ('düz eğlence birimleri', 'sabit oyunlar'),
    ('düz eğlence biriminin', 'sabit oyunun'),
    ('düz eğlence birimine', 'sabit oyuna'),
    ('düz eğlence birimi', 'sabit oyun'),
    # "Düz Atraksiyon" (Flat Ride'ın eski çevirisi)
    ('Düz Atraksiyonların', 'Sabit Oyunların'),
    ('Düz Atraksiyonlara', 'Sabit Oyunlara'),
    ('Düz Atraksiyonları', 'Sabit Oyunları'),
    ('Düz Atraksiyonlar', 'Sabit Oyunlar'),
    ('Düz Atraksiyonun', 'Sabit Oyunun'),
    ('Düz Atraksiyonu', 'Sabit Oyunu'),
    ('Düz Atraksiyon', 'Sabit Oyun'),
    ('düz atraksiyon', 'sabit oyun'),
    # "Sabit Eğlence" (Flat Rides, isimsiz, birimsiz) - tek başına
    # Bu tehlikeli çünkü "sabit eğlence birimi" önce handle edilmiş olmalı (yukarıda)
    ('Sabit Eğlence', 'Sabit Oyun'),
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

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'{len(changes)} kayıt güncellendi.')
for k, old, new in changes[:5]:
    print(f'\n[{k}]\n  Ö: {old[:100]}\n  S: {new[:100]}')
