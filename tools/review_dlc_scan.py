"""Content2 ve Content4 DLC taraması - Content0'la aynı kurallar."""
import json, re
from collections import defaultdict

FORBIDDEN = {
    'çekici': ['ride', 'attraction', 'coaster'],
    'Çekici': ['Ride', 'Attraction', 'Coaster'],
    'misafir': ['guest'], 'Misafir': ['Guest'],
    'lunapark treni': ['coaster', 'roller coaster'],
    'eğlendirici': ['entertainer'], 'Eğlendirici': ['Entertainer'],
}
ARGO_STRICT = [
    (r'\bvalla\b', 'valla'), (r'\bvallah\b', 'vallah'), (r'\byahu\b', 'yahu'),
    (r'\bof ya[.!?]|\bya[.!?](?!\S)', 'ya (cümle sonu)'),
    (r'\bbe[.!?]|\bbe\s*$', 'be (cümle sonu)'),
    (r'\bkanka\b', 'kanka'), (r'\blan\b', 'lan'), (r'\bulan\b', 'ulan'),
]
# "vay be", "Ay be!" gibi cümle BAŞINDAKİ "be" kullanıcı onaylı
SKIP_PATTERNS = [r'^Font 3D', r'^Font - ', r'Sign - ', r'Hedge - ']

for pack in ['Content2', 'Content4']:
    path = f'translations/{pack}/tr.json'
    try:
        data = json.load(open(path, 'r', encoding='utf-8'))
    except FileNotFoundError:
        print(f'{pack}: dosya yok')
        continue
    strings = data['strings']
    print(f'\n{"="*70}\n{pack}: {len(strings)} kayıt\n{"="*70}')

    issues = defaultdict(list)

    for key, entry in strings.items():
        src = entry.get('source', '') or ''
        tr = entry.get('translation', '') or ''
        if entry.get('status') != 'translated' or not tr or tr == src:
            continue
        if any(re.search(p, src) for p in SKIP_PATTERNS):
            continue
        cat = entry.get('category', '')
        src_low = src.lower()

        for bad, trig in FORBIDDEN.items():
            if bad in tr and any(t in src_low for t in trig):
                issues['forbidden'].append((key, cat, src, tr, bad))
                break

        for pat, label in ARGO_STRICT:
            # "Vay be!" veya "Ay be!" pattern'lerini argo sayma (cümle başı onaylı)
            if label == 'be (cümle sonu)':
                # sadece "Vay be!" değilse flag et
                # Regex "be!" matches. Ama öncesinde "Vay "/"Ay " varsa skip
                if re.search(r'(?:Vay|Ay|ay)\s+be[.!?]', tr):
                    continue
            m = re.search(pat, tr, re.IGNORECASE)
            if m:
                issues['argo'].append((key, cat, src, tr, label))
                break

    by_type = {k: len(v) for k, v in issues.items()}
    print(f'Özet: {by_type}')

    for t, items in issues.items():
        print(f'\n--- {t} ({len(items)}) ---')
        for item in items[:30]:
            k, c, s, tr, l = item
            print(f'[{k}] ({c}) -> {l}')
            print(f'  EN: {s[:140]}')
            print(f'  TR: {tr[:140]}')
            print()

    # JSON rapor
    out = {t: [{'key': k, 'category': c, 'source': s, 'translation': tr, 'flag': l}
               for k, c, s, tr, l in items] for t, items in issues.items()}
    with open(f'reviews/{pack.lower()}_issues.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
