#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

# read
with open('translations/shopitem_translated.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# revert wrong change - Viking Çekici = Viking Hammer (toy), not a ride
data['shopitem_misc_vikinghammer'] = 'Viking Çekici'
print('Reverted to:', repr(data['shopitem_misc_vikinghammer']))

# write back
with open('translations/shopitem_translated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print('Saved.')
