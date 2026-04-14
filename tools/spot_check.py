#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Spot-check specific values after cekici replacement."""
import json

CHECKS = [
    # (file, key, expected_contains)
    ('translations/objectives_b1_translated.json', 'objectives_build', 'Eğlence Birimi Yerleştir'),
    ('translations/objectives_b1_translated.json', 'objectives_buildflatnewrides_viewsingular', 'Sabit Eğlence Birimi'),
    ('translations/objectives_b1_translated.json', 'objectives_buildtransportrides_viewsingular', 'Ulaşım Aracı'),
    ('translations/objectives_b1_translated.json', 'objectives_buildopentransportnewrides_viewsingular', 'Ulaşım Aracı'),
    ('translations/objectives_b1_translated.json', 'objectives_coastercam', 'Eğlence Biriminin Kamera Moduna Gir'),
    ('translations/objectives_b1_translated.json', 'objectives_fixride', 'Eğlence Birimini Tamir Et'),
    ('translations/objective_b1_translated.json', 'objective_category_rides', 'Eğlence Birimleri'),
    ('translations/objective_b1_translated.json', 'objective_condition_name_inspectride', 'Eğlence Biriminin Prestijini İncele'),
    ('translations/objective_b2_translated.json', 'objective_item_trackedridetypeallowed_shooting', 'Yalnızca Nişancı Eğlence Birimleri'),
    ('translations/objective_b2_translated.json', 'objective_item_trackedridetypeallowed_transport', 'Ulaşım Araçları'),
    ('translations/parkmanagement_b1_translated.json', 'parkmanagement_advertrequirement_flat', 'Sabit Eğlence Birimi'),
    ('translations/parkmanagement_b1_translated.json', 'parkmanagement_attractions', 'Eğlence Birimleri'),
    ('translations/infopanel_b2_translated.json', 'infopanel_favouritewaterattraction', 'Eğlence Birimi'),
    ('translations/shopitem_translated.json', 'shopitem_misc_vikinghammer', 'Viking Çekici'),  # must stay!
    ('translations/techtreelabel_translated.json', 'techtreelabel_aquatichammerswing', 'Çekici Sallantısı'),  # must stay!
]

ok = 0
fail = 0
for fp, key, expected in CHECKS:
    with open(fp, encoding='utf-8-sig') as f:
        data = json.load(f)
    val = data.get(key, 'NOT_FOUND')
    if expected in val:
        print(f'  OK: [{key}] = {val!r}')
        ok += 1
    else:
        print(f'  FAIL: [{key}]')
        print(f'    expected to contain: {expected!r}')
        print(f'    actual: {val!r}')
        fail += 1

print(f'\n{ok} OK, {fail} FAIL')
