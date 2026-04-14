"""Flat Ride source'unda olup TR'de 'Sabit Oyun' içermeyen kayıtları bul."""
import json
data = json.load(open('translations/Content0/tr.json', 'r', encoding='utf-8'))
strings = data['strings']

missing = []
for k, v in strings.items():
    src = v.get('source', '')
    tr = v.get('translation', '')
    if not tr or tr == src:
        continue
    # Flat Ride varyantları
    if 'Flat Ride' in src or 'flat ride' in src or 'Flat Rides' in src or 'flat rides' in src:
        if 'Sabit Oyun' not in tr and 'sabit oyun' not in tr:
            missing.append((k, src, tr))

print(f'Eksik: {len(missing)}')
# Kategori bazlı gruplandır
from collections import Counter
cats = Counter(strings[k].get('category','') for k,_,_ in missing)
for c, n in cats.most_common():
    print(f'  {c}: {n}')

# Örnekler
print('\n--- ÖRNEKLER ---')
for k, s, tr in missing[:20]:
    print(f'\n[{k}]')
    print(f'EN: {s[:150]}')
    print(f'TR: {tr[:150]}')

# Tam liste JSON
import json
with open('reviews/flat_ride_missing.json', 'w', encoding='utf-8') as f:
    json.dump([{'key': k, 'source': s, 'translation': tr} for k, s, tr in missing], f, ensure_ascii=False, indent=2)
