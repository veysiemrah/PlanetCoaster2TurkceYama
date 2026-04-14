#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test script for fix_cekici.py"""
import sys
sys.path.insert(0, '.')
from tools.fix_cekici import fix_text

tests = [
    ('Çekici Yerleştir', True),
    ('Çekiciler', True),
    ('Çekicinin Prestiji', True),
    ('{Name} Çekicisinin Kamera Moduna Gir', True),
    ('Düz Çekici İnşa Et', True),
    ('Yeni Bir Düz Çekicisi İnşa Et', True),
    ('Bir {Value} Düz Çekicisi İnşa Et:', True),
    ('Açık Düz Çekici Bulundur', True),
    ('Raylı Çekici', True),
    ('Ulaşım Çekicisi', True),
    ('Ulaşım Çekicileri', True),
    ('Bir Çekiciyi Tamir Et', True),
    ('çekicilik', False),   # dokunulmamalı
    ('çekiciliği', False),  # dokunulmamalı
    ('Çekici Görevlisi', True),
    ('Çekici Fiyatlarını Artır', True),
    ('Çekici Dekorunu İyileştir', True),
    ('Çekici Prestiji', True),
    ('Nişancı Çekicisi Yüksek Skoru', True),
    ('Yalnızca Nişancı Çekicileri', True),
    ('Tüm Raylı Çekiciler', True),
    ('Düz Çekici Bulundur', True),
]

print("=== TEST SONUÇLARI ===\n")
ok_count = 0
for text, should_change in tests:
    result, n = fix_text(text)
    changed = n > 0
    if changed == should_change:
        status = 'OK'
        ok_count += 1
    else:
        status = 'FAIL'
    marker = '*' if not should_change and changed else (' ' if should_change == changed else '!')
    print(f"  [{status}] [{marker}] {repr(text)}")
    if changed:
        print(f"          -> {repr(result)}")
    elif should_change:
        print(f"          BEKLENEN: değişmeli ama değişmedi!")

print(f"\n{ok_count}/{len(tests)} test başarılı")
