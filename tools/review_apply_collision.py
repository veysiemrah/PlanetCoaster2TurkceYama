"""Grup A: çarpışma → çakışma (19 kayıt)
Grup C: splashdown yanlış çeviri düzeltmeleri (4 kayıt)"""
import json, shutil

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review5'
shutil.copy2(SRC, BAK)

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

# Grup A: Tam yeni değerler
FIX_A = {
    # "No Clip" başlığı
    'optionsmenu_collisions': 'Çakışmaları Devre Dışı Bırak',
    # optionsmenu_game_*
    'optionsmenu_game_coastercollision_title': 'Hız Treni Çakışması',
    'optionsmenu_game_ridecollision_title': 'Eğlence Çakışmasını Devre Dışı Bırak',
    'optionsmenu_game_scenerycollision_title': 'Dekor Çakışmasını Devre Dışı Bırak',
    'optionsmenu_game_terraincollision_title': 'Arazi Çakışmasını Devre Dışı Bırak',
    # optionsmenu_globaldisable*
    'optionsmenu_globaldisablecoasterobstruction': 'Hız Treni Çakışmasını Devre Dışı Bırak',
    'optionsmenu_globaldisablerideobstruction': 'Eğlence Çakışmasını Devre Dışı Bırak',
    'optionsmenu_globaldisablesceneryobstruction': 'Dekor Çakışmasını Devre Dışı Bırak',
    'optionsmenu_globaldisableterrainobstruction': 'Arazi Çakışmasını Devre Dışı Bırak',
    # sandboxsettings
    'sandboxsettings_category_constructioncollision_label': 'İnşaat Çakışma Ayarları',
    'sandboxsettings_setting_enablecoastercollision_label': 'Hız Treni Çakışması',
    'sandboxsettings_setting_enableflumecollision_label': 'Su Kaydırağı Çakışması',
    'sandboxsettings_setting_enablepathcollision_label': 'Yol Çakışması',
    'sandboxsettings_setting_enablepoolcollision_label': 'Havuz Çakışması',
    'sandboxsettings_setting_enableridecollision_label': 'Düz Oyun Çakışması',
    'sandboxsettings_setting_enablescenerycollision_label': 'Dekor Çakışması',
    'sandboxsettings_setting_enableterraincollision_label': 'Arazi Çakışması',
    'sandboxsettings_setting_enableterrainwatercollision_label': 'Arazi Suyu Çakışması',
}

# "No Clip" (33380) - key'i bulmak için source ile aratıyoruz
NO_CLIP_KEY = None
for k, v in strings.items():
    if v.get('source') == 'No Clip' and v.get('translation') == 'Çarpışma Yok':
        NO_CLIP_KEY = k
        break
if NO_CLIP_KEY:
    FIX_A[NO_CLIP_KEY] = 'Çakışma Yok'
    print(f'  "No Clip" key: {NO_CLIP_KEY}')

# Grup C: splashdown düzeltmeleri
FIX_C = {
    'trackelementname_logsplashcustom': 'Özel Su İnişi',
    'trackelementname_logsplashend': 'Su İnişi Sonu',
    'trackelementname_logsplashmid': 'Su İnişi Orta Bölüm',
    'trackelementname_logsplashstart': 'Su İnişi Başlangıç',
}

all_fixes = {**FIX_A, **FIX_C}
changed = 0
for k, v in all_fixes.items():
    if k not in strings:
        print(f'  UYARI: {k} bulunamadı')
        continue
    old = strings[k]['translation']
    if old != v:
        strings[k]['translation'] = v
        changed += 1
        print(f'  OK {k}: {old[:40]} -> {v[:40]}')

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'\n{changed}/{len(all_fixes)} güncellendi. Yedek: {BAK}')
