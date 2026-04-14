import json, random
for pack in ['Content2', 'Content4']:
    data = json.load(open(f'translations/{pack}/tr.json', 'r', encoding='utf-8'))
    strings = data['strings']
    items = [(k, v) for k, v in strings.items()
             if v.get('translation') and v.get('source') != v.get('translation')]
    print(f'\n=== {pack} - çevrilmiş: {len(items)}/{len(strings)} ===')
    sample = random.sample(items, min(8, len(items)))
    for k, v in sample:
        print(f'[{k}] cat={v.get("category","")}')
        print(f'  EN: {v["source"][:100]}')
        print(f'  TR: {v["translation"][:100]}')
        print()
