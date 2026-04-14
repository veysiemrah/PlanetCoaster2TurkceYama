"""fix_cekici.py'nin fix_text fonksiyonunu test eder"""
import sys
sys.path.insert(0, '.')
from tools.fix_cekici import fix_text, SPECIAL_VALUE, SPECIAL_KEY

sc = '\u00e7'
bc = '\u00c7'

test_cases = [
    # (giris, beklenen_cikis, should_change)
    (sc + 'ekicinin durumu', 'e\u011flence biriminin durumu', True),
    (sc + 'ekiciye bindi', 'e\u011flence birimine bindi', True),
    (sc + 'ekiciyi g\u00f6rd\u00fc', 'e\u011flence birimini g\u00f6rd\u00fc', True),
    (sc + 'ekicide bekledi', 'e\u011flence biriminde bekledi', True),
    (sc + 'ekicideki ziyaret\u00e7i', 'e\u011flence birimindeki ziyaret\u00e7i', True),
    (sc + 'ekiciler parka geldi', 'e\u011flence birimleri parka geldi', True),
    (bc + 'ekicinin prestiji', 'E\u011flence Biriminin prestiji', True),
    (bc + 'ekiciler ve cazibe', 'E\u011flence Birimleri ve cazibe', True),
    (bc + 'ekici itibar\u0131', 'E\u011flence Birimi itibar\u0131', True),
    # Dative plural (Cekicilere Git)
    (bc + 'ekicilere Git', 'E\u011flence Birimlerine Git', True),
    (sc + 'ekicilere bindi', 'e\u011flence birimlerine bindi', True),
    # Ablative (cekiciden ateslendi)
    ('Bu ' + sc + 'ekiciden ate\u015f', 'Bu e\u011flence biriminden ate\u015f', True),
    # Possessive (cekicisi)
    ('Su ' + sc + 'ekicisi say\u0131s\u0131', 'Su e\u011flence birimisi say\u0131s\u0131', True),
    # DOKUNULMAYANLAR:
    (sc + 'ekicilik', sc + 'ekicilik', False),
    (sc + 'ekicilik\u011fi', sc + 'ekicilik\u011fi', False),  # cekicligi (appeal)
    (sc + 'ekicili\u011fini', sc + 'ekicili\u011fini', False),
    (sc + 'ekicilikler', sc + 'ekicilikler', False),
    # Bilesik isimler - bunlar degismeli:
    (bc + 'ekici Foto\u011fraf Kameras\u0131', 'E\u011flence Birimi Foto\u011fraf Kameras\u0131', True),
    (bc + 'ekici G\u00f6revlisi', 'E\u011flence Birimi G\u00f6revlisi', True),
    (bc + 'ekiciler ve Cazibe Merkezleri', 'E\u011flence Birimleri ve Cazibe Merkezleri', True),
    # Kisisel kombinasyonlar
    ('Bu ' + sc + 'ekicinin Ziyaret\u00e7ilere olan ' + bc + 'ekicili\u011fini',
     'Bu e\u011flence biriminin Ziyaret\u00e7ilere olan ' + bc + 'ekicili\u011fini', True),
    # "\n" icindeki
    ('Eskiyen ' + sc + 'ekiciler, Eski olana kadar',
     'Eskiyen e\u011flence birimleri, Eski olana kadar', True),
]

passed = 0
failed = 0
for inp, expected, should_change in test_cases:
    result, count = fix_text(inp)
    changed = result != inp
    if result == expected:
        status = 'PASS'
        passed += 1
    else:
        status = 'FAIL'
        failed += 1
    print(f"[{status}] IN:  {inp!r}")
    if status == 'FAIL':
        print(f"      EXP: {expected!r}")
        print(f"      GOT: {result!r}")
    else:
        print(f"      OUT: {result!r}")
    print()

print(f"\n{passed} passed, {failed} failed")
