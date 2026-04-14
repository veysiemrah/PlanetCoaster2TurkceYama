"""guest_thought sentiment/üslup düzeltmeleri."""
import json, shutil

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review3'
shutil.copy2(SRC, BAK)

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

FIX = {
    'guest_thought_facilityqueuefull_child_01': 'Offf! {reference} çok kalabalık',
    'guest_thought_fluff_badtheming_child_04': 'Ahh! Hiç dekorasyon yok!',
    'guest_thought_goinghome_child_01': 'Offf! Daha gitmek istemiyorum!',
    'guest_thought_inqueue_breakdown_child_01': 'Eyvah! {reference} bozuldu!',
    'guest_thought_assessment_goodride_teen_04': '{reference} çok havalı görünüyor!',
    'guest_thought_shopitem_needsatisfied_hunger_child_03': 'Mis mis, karnıma girdi!',
}

for k, v in FIX.items():
    old = strings[k]['translation']
    strings[k]['translation'] = v
    print(f'OK {k}')
    print(f'   Önce: {old}')
    print(f'   Sonra: {v}')

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'\n{len(FIX)} kayıt güncellendi. Yedek: {BAK}')
