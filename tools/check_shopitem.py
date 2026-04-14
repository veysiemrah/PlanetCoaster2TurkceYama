#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
with open('translations/shopitem_translated.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
print(repr(data.get('shopitem_misc_vikinghammer', 'NOT FOUND')))
