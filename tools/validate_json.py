#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys

files = [
    'translations/objectives_b1_translated.json',
    'translations/objective_b1_translated.json',
    'translations/objective_b2_translated.json',
    'translations/parkmanagement_b1_translated.json',
    'translations/infopanel_b2_translated.json',
    'translations/shopitem_translated.json',
    'translations/techtreelabel_translated.json',
]

ok = True
for fp in files:
    try:
        with open(fp, encoding='utf-8-sig') as f:
            data = json.load(f)
        print(f'OK ({len(data)} keys): {fp}')
    except Exception as e:
        print(f'ERROR: {fp}: {e}')
        ok = False

sys.exit(0 if ok else 1)
