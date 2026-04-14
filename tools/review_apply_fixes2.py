"""
Tutorial düzeltmeleri v2 - glossary'ye tam uyum
"""
import json
import shutil

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review2'
shutil.copy2(SRC, BAK)
print(f'Yedek: {BAK}')

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

FULL_REPLACEMENTS = {
    'tutorialscreen_description_ridetypescoasters':
        'Hız trenleri her tema parkının gözdesidir!\n\nBir Hız Treninin cazibesi, HKB ve Dekorasyon Puanı tarafından belirlenen Prestijiyle temsil edilir. Prestij ne kadar yüksekse, o hız trenine ilgi duyan ziyaretçi sayısı da o kadar fazla olur.\n\nHız trenleri Hazır Şablonlarla veya Özel Hız Treni oluşturularak yerleştirilebilir!\n\nBir Hız Trenindeki vagon sayısını ve operasyonel modlarını değiştirebilirsin. Bu, bir anda kaç ziyaretçinin binebileceğini doğrudan etkiler.\n\nHız trenleri pahalı olabilir; bu yüzden birini satın almak için yeterli paran olduğundan emin ol!',
    'tutorialscreen_description_ridetypesflatride':
        'Sabit Eğlence Birimleri her iyi tema parkının vazgeçilmezidir!\n\nBir Sabit Eğlence Biriminin cazibesi, Dekorasyon Puanıyla birlikte Heyecan, Korku ve Mide Bulantısı puanlarıyla belirlenen Prestijinde yansıtılır. Bir Sabit Eğlence Biriminin HKB\'si, Hareket Sırasına göre belirlenir.\n\nSabit Eğlence Birimleri, dekor içeren Hazır Şablonlar seçilerek veya "Özel Oluştur" seçeneğiyle yerleştirilebilir.',
    'tutorialscreen_description_ridetypestrack':
        'Raylı Eğlence Birimleri, Hız Trenleriyle birçok benzerlik paylaşır.\n\nBir Raylı Eğlence Biriminin cazibesi, HKB ve Dekorasyon Puanı tarafından belirlenen Prestijiyle temsil edilir.\n\nRaylı Eğlence Birimleri ray üzerinde sabit bir hızda ilerler. Bu hızı Operasyonlar menüsünden değiştirebilirsin.\n\nRaylı Eğlence Birimleri de hız trenlerine benzer şekilde inşa edilir; ancak ray açıları daha kısıtlıdır. Bu nedenle Raylı Eğlence Birimleri genellikle hız trenlerine kıyasla daha sakin bir deneyim sunar.',
}

changed = 0
for key, new_tr in FULL_REPLACEMENTS.items():
    old = strings[key]['translation']
    if old == new_tr:
        continue
    strings[key]['translation'] = new_tr
    changed += 1
    print(f'  OK: {key}')

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\nToplam: {changed} değişiklik kaydedildi.')
