import json
d = json.load(open('translations/Content0/tr.json', 'r', encoding='utf-8'))
keys = ['tutorialscreen_description_ridetypescoasters',
        'tutorialscreen_description_ridetypesflatride',
        'tutorialscreen_description_ridetypestrack']
for k in keys:
    e = d['strings'][k]
    print(f'=== {k} ===')
    print('EN:', e['source'])
    print('TR:', e['translation'])
    print()
