"""
vo_* voice-over taraması.
Kontroller:
 1. sentiment=Happy/Sad/Shocked/Fear/Angry/Neutral tag'i ile TR uyumsuz
 2. İngilizce ünlem kalıntıları ("Aw", "Oh", "Gee" vb. çevrilmeden kalmış)
 3. Üzüntü sentiment'ı olan yerde sevinçli ifadeler ("Yay", "Harika")
 4. Literal çeviri riskli deyimler
 5. Çevrilmemiş kayıtlar
"""
import json, re
from collections import defaultdict

data = json.load(open('translations/Content0/tr.json', 'r', encoding='utf-8'))
strings = data['strings']

vo = {k: v for k, v in strings.items() if v.get('category') == 'vo'}
print(f'Toplam vo: {len(vo)}')

issues = defaultdict(list)

# Sentiment-sevinç/üzüntü eşleşmezlik kelimeleri
JOY_WORDS = ['harika', 'müthiş', 'süper', 'enfes', 'vay be', 'ne güzel', 'muhteşem',
             'yaşasın', 'dayanamıyorum', 'sevin', 'mutlu', 'inanılmaz', 'efsane']
SAD_WORDS = ['eyvah', 'yazık', 'kötü', 'berbat', 'üzgün', 'üzüldüm', 'olamaz',
             'of', 'ah', 'ahh', 'moralim', 'umutsuz', 'korkunç', 'endişe']
FEAR_WORDS = ['eyvah', 'korkut', 'korkunç', 'ürperti', 'tüyler', 'amanın', 'aman tanrım',
              'of', 'ah ', 'endişe', 'panik']

# İngilizce kalıntı: çeviride olmaması gereken İngilizce başlayıcı ünlemler
ENGLISH_INTERJECTIONS = [
    r'^Aw\b', r'^Aww\b', r'^Oh\s+(?!hayır|tanrım)', r'^Oh,\s', r'^Gee\b', r'^Yay\b',
    r'^Yikes\b', r'^Whoa\b', r'^Woah\b(?!\s+ho)', r'^Hooray\b', r'^Boy\b(?=\s*[,!])',
    r'^Man\b(?=\s*[,!])', r'^Whoopsie\b', r'^Phew\b',
]

UNTRANSLATED_SHORT = []

for key, entry in vo.items():
    src = entry.get('source', '') or ''
    tr = entry.get('translation', '') or ''
    if entry.get('status') != 'translated' or not tr:
        continue
    if tr == src and len(src) > 10:
        issues['untranslated'].append((key, src, tr, 'identical'))
        continue

    # Sentiment tag
    m = re.search(r'\[sentiment=(\w+)\]', src)
    sentiment = m.group(1).lower() if m else None
    tr_clean = re.sub(r'\[sentiment=\w+\]', '', tr).strip().lower()
    src_clean = re.sub(r'\[sentiment=\w+\]', '', src).strip().lower()

    # İngilizce kalıntı kontrolü
    for pat in ENGLISH_INTERJECTIONS:
        if re.search(pat, tr):
            issues['english_residue'].append((key, src, tr, re.search(pat, tr).group(0)))
            break

    # Sentiment-tone uyumsuzluğu
    if sentiment in ('sad', 'fear', 'angry'):
        # Üzücü/korku bağlamında sevinçli kelime var mı?
        found_joy = [w for w in JOY_WORDS if w in tr_clean]
        # Ama "harika bir felaket" gibi sarkastik kullanım olabilir, conservative ol
        if found_joy and not any(w in src_clean for w in ['great', 'wonderful', 'amazing', 'awesome', 'fantastic', 'love']):
            issues['sentiment_mismatch_joy'].append((key, src, tr, f'{sentiment}:{found_joy}'))

    if sentiment == 'happy':
        # Mutlu bağlamda üzüntü kelimesi
        found_sad = [w for w in SAD_WORDS if w in tr_clean]
        if found_sad and not any(w in src_clean for w in ['oh no', 'sorry', 'sad', 'terrible', 'bad', 'worry']):
            issues['sentiment_mismatch_sad'].append((key, src, tr, f'{sentiment}:{found_sad}'))

# Rapor
print('\n=== ÖZET ===')
for t, items in sorted(issues.items(), key=lambda x: -len(x[1])):
    print(f'  {t}: {len(items)}')

out = {t: [{'key': k, 'source': s, 'translation': tr, 'detail': d}
           for k, s, tr, d in items] for t, items in issues.items()}
with open('reviews/content0_vo_issues.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print('\nRapor: reviews/content0_vo_issues.json')
