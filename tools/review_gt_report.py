"""Gerçek guest_thought sorunlarını oku ve yazdır."""
import json
rep = json.load(open('reviews/content0_gt_issues.json', 'r', encoding='utf-8'))

skip = {'english_leak'}

for label, items in rep.items():
    if label in skip:
        continue
    print(f'\n=== {label.upper()} ({len(items)}) ===')
    for item in items:
        print(f"[{item['key']}]")
        print(f"  EN: {item['source']}")
        print(f"  TR: {item['translation']}")
        if 'match' in item:
            print(f"  MATCH: {item['match']}")
        print()
