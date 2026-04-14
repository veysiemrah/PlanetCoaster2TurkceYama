#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify no unwanted cekici remains in translation files."""
import json
import sys

FILES = [
    'translations/objectives_b1_translated.json',
    'translations/objective_b1_translated.json',
    'translations/objective_b2_translated.json',
    'translations/parkmanagement_b1_translated.json',
    'translations/infopanel_b2_translated.json',
    'translations/shopitem_translated.json',
    'translations/techtreelabel_translated.json',
]

# These are OK to remain as-is (hammer/appeal meanings)
ALLOWED_SUBSTRINGS = [
    'çekicilik',
    'çekiciliği',
    'çekiciliğini',
    'çekiciliğine',
    'Viking Çekici',
    'viking çekici',
    'Su Çekici Sallantısı',
    'su çekici sallantısı',
    'Çekici Sallantısı',   # hammer swing in ride names
]

total_issues = 0
for fp in FILES:
    try:
        with open(fp, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
    except Exception as e:
        print(f'ERROR reading {fp}: {e}')
        continue

    issues = []
    for key, val in data.items():
        if not isinstance(val, str):
            continue
        lower = val.lower()
        if 'çekici' not in lower:
            continue
        # check against allowed substrings
        allowed_ok = any(a.lower() in lower for a in ALLOWED_SUBSTRINGS)
        if not allowed_ok:
            issues.append(f'  [{key}] = {val!r}')

    if issues:
        print(f'\nSORUNLAR: {fp}')
        for i in issues:
            print(i)
        total_issues += len(issues)
    else:
        print(f'OK: {fp}')

print(f'\nToplam sorun: {total_issues}')
sys.exit(0 if total_issues == 0 else 1)
