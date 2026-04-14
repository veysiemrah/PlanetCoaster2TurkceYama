"""
Content0 review düzeltmelerini uygular:
- TIER 1 argo
- TIER 1 sandboxsettings çekicilik
- Tutorial düzeltmeleri
- Glossary güncellemesi (Appeal, Track Ride, Ride Sequence)
"""
import json
import shutil

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review1'

# Yedek
shutil.copy2(SRC, BAK)
print(f'Yedek: {BAK}')

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

# (key, expected_old_substring, new_full_translation) formatında değiller;
# bazıları tam değiştirme, bazıları replace. İki tip yapıyorum.

# Tam değiştirmeler
FULL_REPLACEMENTS = {
    'guest_thought_nauseacritical_natural_teen_01': 'Kusacak gibiyim!',
    'guest_thought_toiletcritical_natural_teen_03': 'Çok tuvaletim var',
    'guest_thought_vomited_teen_02': 'Yediğim her şeyi kustum',
    'guest_thought_nauseacritical_natural_adult_02': 'Midem bulanıyor',
    'guest_thought_nobenches_common_02': 'Burada hiç bank yok mu?',
    'guest_thought_fluff_badridetheming_adult_02': '{reference} üzerinde neredeyse hiç dekorasyon yok!',
    'guest_thought_fluff_onride_intensityhigh_adult_03': 'Amanın! Çok korkutucu bir andı! - {reference}',
    'guest_thought_sunburn_common_01': 'Eyvah! Çok fazla güneşte kaldım! Güneş kremi bulmam lazım!',
    'guest_thought_queuefull_teen_02': "Of ya! {reference}'in sırası tamamen dolmuş!",
    'sandboxsettings_category_waterpark_description': 'Su parkı aktivitelerinin işleyişini etkileyen ayarlar.',
    'sandboxsettings_setting_preferencesenabled_description':
        'Ziyaretçiler parka kendilerine özgü tercihlerle gelir; bu tercihler ilgi duydukları aktiviteleri ve nelerden zevk alacaklarını etkiler.\n\nDevre dışı bırakılırsa ziyaretçiler belirli bir tercih olmadan parka gelir ve her şeyden olduğu gibi zevk alır.',
    'tutorialscreen_description_ridetypescoasters':
        'Hız trenleri her tema parkının gözdesidir!\n\nBir Hız Treninin cazibesi, HKB ve Dekor Puanı tarafından belirlenen İtibarıyla ölçülür. İtibar ne kadar yüksekse, o hız trenine ilgi duyan ziyaretçi sayısı da o kadar fazla olur.\n\nHız trenleri Hazır Planlarla veya Özel Hız Treni oluşturularak yerleştirilebilir!\n\nBir Hız Trenindeki vagon sayısını ve operasyonel modlarını değiştirebilirsin. Bu, bir anda kaç ziyaretçinin binebileceğini doğrudan etkiler.\n\nHız trenleri pahalı olabilir; bu yüzden birini satın almak için yeterli paran olduğundan emin ol!',
    'tutorialscreen_description_ridetypesflatride':
        'Sabit Eğlence Birimleri her iyi tema parkının vazgeçilmezidir!\n\nBir Sabit Eğlence Biriminin cazibesi, Dekor Puanıyla birlikte Heyecan, Korku ve Bulantı puanlarıyla belirlenen İtibarında yansıtılır. Bir Sabit Eğlence Biriminin HKB\'si, Hareket Sırasına göre belirlenir.\n\nSabit Eğlence Birimleri, dekor içeren Hazır Planlar seçilerek veya "Özel Oluştur" seçeneğiyle yerleştirilebilir.',
    'tutorialscreen_description_ridetypestrack':
        'Raylı Eğlence Birimleri, Hız Trenleriyle birçok benzerlik paylaşır.\n\nBir Raylı Eğlence Biriminin cazibesi, HKB ve Dekor Puanı tarafından belirlenen İtibarıyla ölçülür.\n\nRaylı Eğlence Birimleri ray üzerinde sabit bir hızda ilerler. Bu hızı Operasyonlar menüsünden değiştirebilirsin.\n\nRaylı Eğlence Birimleri de hız trenlerine benzer şekilde inşa edilir; ancak ray açıları daha kısıtlıdır. Bu nedenle Raylı Eğlence Birimleri genellikle hız trenlerine kıyasla daha sakin bir deneyim sunar.',
}

changed = 0
for key, new_tr in FULL_REPLACEMENTS.items():
    if key not in strings:
        print(f'  UYARI: {key} bulunamadı')
        continue
    old = strings[key]['translation']
    if old == new_tr:
        print(f'  SKIP (aynı): {key}')
        continue
    strings[key]['translation'] = new_tr
    changed += 1
    print(f'  OK: {key}')
    print(f'     ÖNCE: {old[:100]}')
    print(f'     SONRA: {new_tr[:100]}')

# Kaydet
with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\nToplam değişiklik: {changed}')
print(f'Dosya kaydedildi: {SRC}')
