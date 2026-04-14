import json
d = json.load(open('translations/Content0/tr.json', 'r', encoding='utf-8'))
strings = d['strings']
print('Strings count:', len(strings))
sample_keys = list(strings.keys())[:5]
for k in sample_keys:
    print(f'\n--- {k} ---')
    print(repr(strings[k])[:300])
