"""
Glossary tutarlılık taraması v2 - false positive'ler elendi
"""
import json
import re
from collections import defaultdict

glossary = json.load(open('glossary.json', 'r', encoding='utf-8'))['terms']
data = json.load(open('translations/Content0/tr.json', 'r', encoding='utf-8'))
strings = data['strings']

# Yasak terimler (kesin yanlış kullanımlar)
FORBIDDEN = {
    'çekici': ['ride', 'attraction', 'coaster'],
    'Çekici': ['Ride', 'Attraction', 'Coaster'],
    'misafir': ['guest'],
    'Misafir': ['Guest'],
    'lunapark treni': ['coaster', 'roller coaster'],
    'eğlendirici': ['entertainer'],
    'Eğlendirici': ['Entertainer'],
}

# Argo — sadece cümle SONUNDA veya tek başına kullanımı yasak
# "ya da" / "ya X ya Y" meşru bağlaç, atla
ARGO_STRICT = [
    (r'\bvalla\b', 'valla'),
    (r'\bvallah\b', 'vallah'),
    (r'\byahu\b', 'yahu'),
    (r'\bvay be\b', 'vay be'),
    (r'\bof ya\b', 'of ya (cümle sonu)'),
    (r'\bbe[.!?]', 'be (cümle sonu)'),
    (r'\bya[.!?]', 'ya (cümle sonu)'),
    (r'\bkanka\b', 'kanka'),
    (r'\blan\b', 'lan'),
    (r'\bulan\b', 'ulan'),
    (r'\beyvallah\b', 'eyvallah'),
]

# Font/özel ad kaynak bulmak için - "Font 3D - Coaster X" gibi
SKIP_PATTERNS = [
    r'^Font 3D',
    r'^Font - ',
    r'Sign - ',
    r'Hedge - ',
]

issues = defaultdict(list)

for key, entry in strings.items():
    src = entry.get('source', '') or ''
    tr = entry.get('translation', '') or ''
    status = entry.get('status', '')
    cat = entry.get('category', '')

    if status != 'translated' or not tr or tr == src:
        continue

    # Font/özel ad atla
    if any(re.search(p, src) for p in SKIP_PATTERNS):
        continue

    src_lower = src.lower()
    tr_lower = tr.lower()

    # 1) Yasak terim
    for bad, triggers in FORBIDDEN.items():
        if bad in tr:
            if any(t in src_lower for t in triggers):
                issues['forbidden_term'].append((key, cat, src, tr, bad))
                break

    # 2) Argo (sıkı)
    for pat, label in ARGO_STRICT:
        if re.search(pat, tr, re.IGNORECASE):
            issues['argo'].append((key, cat, src, tr, label))
            break

# Kategori bazlı özet
print('=' * 80)
print('GLOSSARY TUTARLILIK TARAMASI v2 - Content0')
print('=' * 80)

for issue_type, items in issues.items():
    # Kategoriye göre grupla
    by_cat = defaultdict(list)
    for item in items:
        by_cat[item[1]].append(item)

    print(f'\n### {issue_type.upper()} - TOPLAM {len(items)}')
    for cat, cat_items in sorted(by_cat.items(), key=lambda x: -len(x[1])):
        print(f'  {cat or "(boş)"}: {len(cat_items)}')

# Detay
print('\n' + '=' * 80)
print('DETAYLAR')
print('=' * 80)

for issue_type, items in issues.items():
    print(f'\n\n### {issue_type.upper()} DETAY')
    for item in items:
        key, cat, src, tr, label = item
        print(f'\n[{key}] (cat={cat}) -> {label}')
        print(f'  EN: {src[:150]}')
        print(f'  TR: {tr[:150]}')

# JSON raporu yaz
report = {
    'forbidden_term': [{'key': k, 'category': c, 'source': s, 'translation': t, 'flag': l}
                       for k, c, s, t, l in issues.get('forbidden_term', [])],
    'argo': [{'key': k, 'category': c, 'source': s, 'translation': t, 'flag': l}
             for k, c, s, t, l in issues.get('argo', [])],
}
with open('reviews/content0_glossary_issues.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(f'\n\nRapor: reviews/content0_glossary_issues.json')
