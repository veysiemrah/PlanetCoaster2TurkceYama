"""
guest_thought kategorisinde anlam/üslup sorunlarını tespit eder.
Heuristicler:
 1. Awkward kalıplar: "{ref} X görünüyor" gibi İngilizce "looks X" birebir çevirileri
 2. Çeviri = kaynak (çevrilmemiş)
 3. Anormal uzunluk oranı (çok uzun/çok kısa)
 4. İngilizce kelime kalıntıları
 5. Şüpheli "ya" kullanımı (virgülden önce, cümle sonuna yakın)
 6. Deyim bozuklukları ("blew chunks", "I'm busting" gibi)
 7. Duplicated words
 8. Yanlış zaman/kip karışımı
"""
import json
import re
from collections import defaultdict

data = json.load(open('translations/Content0/tr.json', 'r', encoding='utf-8'))
strings = data['strings']

gt = {k: v for k, v in strings.items() if v.get('category') == 'guest_thought'}
print(f'Toplam guest_thought: {len(gt)}')

issues = defaultdict(list)

AWKWARD_PATTERNS = [
    (r'vay be\s+görünüyor', 'awkward_vay_be'),
    (r'\b(\w+)\s+\1\b', 'repeated_word'),  # aynı kelime peşpeşe
    (r'\bkanka\b|\blan\b|\bulan\b', 'hard_slang'),
    (r'of ya[.!?]|\bya[.!?]', 'ya_sentence_end'),
    (r'\bbe[.!?]', 'be_sentence_end'),
    (r'\bya+y', 'stutter_ya'),  # "yaya" "yayay"
    (r'\byahu\b|\bvalla\b', 'forbidden_slang'),
    (r'[a-zA-Z]{5,}[^\w\s\']', 'english_leak'),  # 5+ letter ASCII word (ref placeholders vs)
]

SHORT_SRC_LONG_TR_RATIO = 2.5  # Türkçe genelde kısadır

for key, entry in gt.items():
    src = entry.get('source', '') or ''
    tr = entry.get('translation', '') or ''

    if not tr or entry.get('status') != 'translated':
        continue

    # Placeholder'ları çıkararak ölç
    src_clean = re.sub(r'\{[^}]+\}', 'X', src).strip()
    tr_clean = re.sub(r'\{[^}]+\}', 'X', tr).strip()

    # 1) Çevrilmemiş
    if src == tr and len(src) > 5:
        issues['untranslated'].append((key, src, tr))
        continue

    # 2) Pattern bazlı
    for pat, label in AWKWARD_PATTERNS:
        m = re.search(pat, tr, re.IGNORECASE)
        if m:
            # english_leak için, "Wow", "OK" vs sistemsel kalıntıları hariç tut
            if label == 'english_leak':
                # placeholder ya da alfabe dışı mı? Atla
                matched = m.group(0)
                # Türkçe karakter içeriyorsa zaten Türkçe sayılır
                if re.search(r'[çğıöşüÇĞİÖŞÜ]', matched):
                    continue
                # Bariz İngilizce değilse atla
                if matched.lower() in ['olmak', 'bakmak', 'sahiptir', 'yapar']:
                    continue
            issues[label].append((key, src, tr, m.group(0)))

    # 3) Uzunluk sapması
    if len(src_clean) > 20 and len(tr_clean) > len(src_clean) * SHORT_SRC_LONG_TR_RATIO:
        issues['too_long_tr'].append((key, src, tr, len(src_clean), len(tr_clean)))

    # 4) "X görünüyor" biçimi, yabancı yapı
    if re.search(r'\{[^}]+\}\s+(?!çok|ne|harika|güzel|kötü|berbat)[\w]+\s+görünüyor', tr, re.IGNORECASE):
        # "{ref} yaşlı görünüyor" → doğal. "{ref} vay be görünüyor" → değil.
        # Sade regex yerine, "görünüyor"dan önceki kelimeyi kontrol et
        pass  # şimdilik skip, çok gürültülü

# Özet
print('\n=== SORUN ÖZETİ ===')
for label, items in sorted(issues.items(), key=lambda x: -len(x[1])):
    print(f'  {label}: {len(items)}')

# Rapor yaz
out = {}
for label, items in issues.items():
    out[label] = []
    for item in items[:100]:
        if len(item) == 3:
            out[label].append({'key': item[0], 'source': item[1], 'translation': item[2]})
        elif len(item) == 4:
            out[label].append({'key': item[0], 'source': item[1], 'translation': item[2], 'match': item[3]})
        else:
            out[label].append({'key': item[0], 'source': item[1], 'translation': item[2],
                               'src_len': item[3], 'tr_len': item[4]})

with open('reviews/content0_gt_issues.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print('\nRapor: reviews/content0_gt_issues.json')
