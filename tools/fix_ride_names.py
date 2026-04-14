"""Eglence birimi isimlerini tutarli hale getir.

Kurallar:
- Teacups, Tiny Eye, Boardslide vb. marka/model adlari orijinal kalir
- Dönme Dolap, Atlıkarınca, Maden Treni vb. kabul görmüş Türkçe adlar çevrilir
- Su kaydırak türleri water_ ile tutarlı: Lastik Halkalı Kaydırak vb.
"""
import json
import shutil
from pathlib import Path

tr_path = Path("../translations/Content0/tr.json")
backup = tr_path.with_suffix(".json.bak_ridenames")

if not backup.exists():
    shutil.copy(tr_path, backup)
    print(f"Yedek: {backup.name}")

data = json.loads(tr_path.read_text(encoding="utf-8"))
strings = data["strings"]

# key -> new_translation eslestirmeleri
FIXES = {
    # === Teacups (orijinal) ===
    "fr_teacups": "Teacups",
    "pc_flatride_teacups": "Planet Coaster Teacups",
    "my_flatride_teacups": "Mythology Teacups",
    "aq_flatride_teacups": "Aquatic Teacups",
    "re_flatride_teacups": "Resort Teacups",
    "re_flatride_teacups_desc": "Resort temalı Teacups eğlencesi.",
    "vi_flatride_teacups": "Viking Teacups",
    "vi_flatride_teacups_desc": "Viking temalı Teacups eğlencesi.",
    "techtreelabel_teacups": "Teacups",
    "techtreelabel_resortteacups": "Resort Teacups",
    "techtreelabel_aquaticteacups": "Aquatic Teacups",
    "semantictag_teacup1": "Teacup 1",
    "semantictag_teacup2": "Teacup 2",
    "semantictag_teacup3": "Teacup 3",
    "semantictag_teacup4": "Teacup 4",

    # === Tiny Eye (orijinal) ===
    "techtreelabel_aquatictinyeye": "Aquatic Tiny Eye",

    # === Boardslide (orijinal marka/model) ===
    "techtreelabel_boardslide": "Boardslide",
    "techtreelabel_mythologyboardslide": "Mythology Boardslide",
    "techtreelabel_resortboardslide": "Resort Boardslide",

    # === Buoyancy (orijinal marka) ===
    "techtreelabel_buoyancy": "Buoyancy",
    "techtreelabel_aquaticbuoyancy": "Aquatic Buoyancy",

    # === Collider (orijinal marka) ===
    "techtreelabel_collider": "Collider",
    "techtreelabel_aquaticcollider": "Aquatic Collider",

    # === Forge (orijinal marka) ===
    "techtreelabel_forge": "Forge",
    "techtreelabel_aquaticforge": "Aquatic Forge",
    "techtreelabel_resortforge": "Resort Forge",

    # === Hammer Swing (orijinal) ===
    "techtreelabel_hammerswing": "Hammer Swing",
    "techtreelabel_aquatichammerswing": "Aquatic Hammer Swing",

    # === Monsoon Chute (orijinal) ===
    "techtreelabel_monsoonchute": "Monsoon Chute",
    "techtreelabel_aquaticmonsoonchute": "Aquatic Monsoon Chute",
    "re_flatride_monsoonchute": "Resort Monsoon Chute",
    "techtreelabel_resortmonsoonchute": "Resort Monsoon Chute",

    # === Polarity (orijinal) ===
    "techtreelabel_polarity": "Polarity",
    "techtreelabel_resortpolarity": "Resort Polarity",

    # === Sky Beam (orijinal) ===
    "techtreelabel_skybeam": "Sky Beam",
    "techtreelabel_vikingskybeam": "Viking Sky Beam",
    "vi_flatride_skybeam": "Viking Sky Beam",

    # === Diğer orijinal kalacak markalar ===
    "techtreelabel_360power": "360 Power",
    "techtreelabel_behemothswing360": "Behemoth Swing 360",
    "techtreelabel_bumpinderby": "Bumpin' Derby",
    "techtreelabel_chairoplane": "Uçan Sandalye",
    "techtreelabel_frenzyfrill": "Frenzy Frill",
    "techtreelabel_fullflight": "Full Flight",
    "techtreelabel_hellionring": "Hellion Ring",
    "techtreelabel_hyperspin": "Hyperspin",
    "techtreelabel_insanity": "Insanity",
    "techtreelabel_mecharoller": "Mecha Roller",
    "techtreelabel_overpower": "Overpower",
    "techtreelabel_parallelogram": "Parallelogram",
    "techtreelabel_radius": "Radius",
    "techtreelabel_resurgence": "Resurgence",
    "techtreelabel_skywatcher": "Sky Watcher",
    "techtreelabel_starwheel": "Star Wheel",
    "techtreelabel_sundial": "Sun Dial",
    "techtreelabel_sunflare": "Sun Flare",
    "techtreelabel_synchronise": "Synchronise",
    "techtreelabel_thescreaminator": "The Screaminator",
    "techtreelabel_twistedarc": "Twisted Arc",
    "techtreelabel_vanguard": "Vanguard",
    "techtreelabel_velocity": "Velocity",
    "techtreelabel_wildblue": "Wild Blue",
    "techtreelabel_thevoid": "The Void",
    "techtreelabel_thedriller": "The Driller",
    "techtreelabel_planetcoastersunflare": "Planet Coaster Sun Flare",
    "techtreelabel_soarer": "Soarer",
    "techtreelabel_hopper": "Hopper",
    "techtreelabel_minder": "Minder",
    "techtreelabel_knotted": "Knotted",
    "techtreelabel_murphyandson": "Murphy and Son",
    "techtreelabel_whitelakeamusementshore": "Whitelake Amusement Shore",
    "techtreelabel_eddiefunmitchellcompany": "Eddie Fun Mitchell Company",
    "techtreelabel_backfire": "Backfire",
    "techtreelabel_dive": "Dive",
    "techtreelabel_inverter": "Inverter",
    "techtreelabel_impulsion": "Impulsion",
    "techtreelabel_singularity": "Singularity",
    "techtreelabel_limitless": "Limitless",
    "techtreelabel_spiralizer": "Spiralizer",
    "techtreelabel_splashdown": "Splashdown",
    "techtreelabel_wing": "Wing",
    "techtreelabel_standup": "Standup",
    "techtreelabel_floorless": "Floorless",
    "techtreelabel_zephyr": "Zephyr",
    "techtreelabel_starloop": "Star Loop",
    "techtreelabel_cloudsurfer": "Cloud Surfer",
    "techtreelabel_dartkinetics": "Dart Kinetics",
    "techtreelabel_flightofthecondor": "Flight of the Condor",
    "techtreelabel_mountaindescent": "Mountain Descent",
    "techtreelabel_groundswell": "Groundswell",
    "techtreelabel_bigmsrides": "FD Vision",
    "techtreelabel_citypeninsula": "City Peninsula",
    "techtreelabel_deepseacontinental": "Deep Sea Continental",
    "techtreelabel_movementconstruction": "Movement Construction",
    "techtreelabel_kingdomisle": "Kingdom Isle",
    "techtreelabel_looping": "Looping",
    "techtreelabel_loopingshuttle": "Looping Shuttle",
    "techtreelabel_twinloops": "Twin Loops",

    # === Kabul görmüş Türkçe adlar (değişiklik yapmadan tutarlı hale getir) ===
    "fr_bigwheel": "Dönme Dolap",
    "techtreelabel_bigwheel": "Dönme Dolap",
    "fr_grandcarousel": "Büyük Atlıkarınca",
    "fr_chairoplane": "Uçan Sandalye",

    # === Su kaydırakları (water_ ile tutarlı yap) ===
    "techtreelabel_innertubeflume": "Lastik Halkalı Kaydırak",
    "techtreelabel_doubleinnertubeflume": "Çift Lastik Halkalı Kaydırak",
    "techtreelabel_matflume": "Minderli Kaydırak",
    "techtreelabel_raftflume": "Sallı Kaydırak",
    "techtreelabel_raftflumeblueprint": "Sallı Kaydırak",
    "techtreelabel_narrowlogflume": "Dar Kütük Kızağı",

    # === Nehir Akıntısı (techtree plural düzelt) ===
    "techtreelabel_riverrapids": "Nehir Akıntısı",

    # === Coaster tipleri (zaten çevrilmiş, tutarlılık kontrolü) ===
    "techtreelabel_boomerang": "Bumerang",
    "techtreelabel_giantinvertedboomerang": "Dev Ters Bumerang",
    "techtreelabel_minetrain": "Maden Treni",
    "techtreelabel_swingingminetrain": "Sallanan Maden Treni",
    "techtreelabel_crazymouse": "Deli Fare",
    "techtreelabel_rowdymouse": "Gürültücü Fare",
    "techtreelabel_spinningwildmouse": "Dönen Vahşi Fare",
    "techtreelabel_wooden_wildmouse": "Vahşi Fare",
    "techtreelabel_juniorcoaster": "Küçük Hız Treni",
    "techtreelabel_rotatingcoaster": "Döner Hız Treni",
    "techtreelabel_spinningcoaster": "Dönen Hız Treni",
    "techtreelabel_splashcoaster": "Sıçrayan Hız Treni",
    "techtreelabel_wavecoaster": "Dalga Hız Treni",
    "techtreelabel_watercoaster": "Su Hız Treni",
    "techtreelabel_antiquewatercoaster": "Antika Su Hız Treni",
    "techtreelabel_acceleratorcoaster": "Hızlandırıcı Hız Treni",
    "techtreelabel_tiltcoaster": "Eğik Hız Treni",
    "techtreelabel_wooden": "Ahşap",
    "techtreelabel_wooden_sidefriction": "Yan Sürtünme",
    "techtreelabel_singlerail": "Tek Ray",

    # === Production company / marka şirketi (orijinal kalsın) ===
    "techtreelabel_murphyrides": "Murphy Rides",
    "techtreelabel_premiumrides": "Premium Rides",
    "techtreelabel_pearlrides": "Pearl Rides",
    "techtreelabel_grandcoastersworldwide": "Grand Coasters Worldwide",
    "techtreelabel_fdenterprises": "FD Enterprises",
    "techtreelabel_fdvision": "FD Vision",
    "techtreelabel_highpeaksconstruction": "High Peaks Construction",
    "techtreelabel_masha": "Masha",
    "techtreelabel_giovanni": "Giovanni",
    "techtreelabel_dazer": "Dazer",
    "techtreelabel_conlan": "Conlan",
    "techtreelabel_anton": "Anton",
    "techtreelabel_powa": "Powa",
    "techtreelabel_khnorter": "K.H Norter",
    "techtreelabel_outamax": "Outamax",
    "techtreelabel_outback": "Outback",
    "techtreelabel_vector": "Vector",
    "techtreelabel_monteleone": "Weisshorn",
    "techtreelabel_animal": "Animal",

    # === fr_ eğlence birimleri — orijinal isimler korunacaksa zaten öyle ===
    "fr_weisshorn": "Monte Leone",
    "fr_thorn": "Splintery",
    # Splintery -> "Diken" yanlış, techtree'de de "Diken" var. Düzelt:
    "techtreelabel_thorn": "Splintery",
}

applied = 0
skipped = []
for key, new_trn in FIXES.items():
    entry = strings.get(key)
    if not entry:
        skipped.append(key)
        continue
    if entry.get("translation") != new_trn:
        entry["translation"] = new_trn
        applied += 1

tr_path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(f"Uygulanan: {applied} / {len(FIXES)}")
if skipped:
    print(f"Anahtar bulunamadi: {len(skipped)}")
    for k in skipped[:10]:
        print(f"  {k}")
