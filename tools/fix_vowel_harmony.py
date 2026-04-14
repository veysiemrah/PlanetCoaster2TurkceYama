import json
d = json.load(open('translations/Content0/tr.json', 'r', encoding='utf-8'))
k = 'vo_eugenenewton_tutorial1_outro_100'
e = d['strings'][k]
e['translation'] = e['translation'].replace('sabit oyunlarin', 'sabit oyunların')
json.dump(d, open('translations/Content0/tr.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK')
