import json
r = json.load(open('reviews/content0_vo_issues.json','r',encoding='utf-8'))
print('=== sentiment_mismatch_joy (3) ===')
for item in r.get('sentiment_mismatch_joy', []):
    print(item['key'])
    print('EN:', item['source'])
    print('TR:', item['translation'])
    print('DETAIL:', item['detail'])
    print()
