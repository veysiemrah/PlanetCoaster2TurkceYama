import json
r = json.load(open('reviews/content0_vo_issues.json','r',encoding='utf-8'))
print(f'Toplam: {len(r["english_residue"])}')
for item in r['english_residue']:
    print('---')
    print(f'KEY: {item["key"]}')
    print(f'EN:  {item["source"]}')
    print(f'TR:  {item["translation"]}')
