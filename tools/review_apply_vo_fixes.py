"""vo_* 'Oh' düzeltmeleri - 30 kayıt."""
import json, shutil

SRC = 'translations/Content0/tr.json'
BAK = 'translations/Content0/tr.json.bak_review4'
shutil.copy2(SRC, BAK)

data = json.load(open(SRC, 'r', encoding='utf-8'))
strings = data['strings']

# Her kayıt için tam yeni TR. [sentiment=X] tag'i korunur.
FIX = {
    'vo_adrianavega_buildingthebifrost_intro_010':
        'Aa, iyi ki geldin! Sana harika haberlerim var! [sentiment=Happy]',
    'vo_adrianavega_chapter2_080':
        'Ah, ne kadar sevindim! Birlikte neler başaracağımızı görmek için sabırsızlanıyorum! ¡Adios! [sentiment=Happy]',
    'vo_adrianavega_labyrinthsecrets_silver_040':
        'Aa, yeraltında mı? Hayır, yıllar önce kaçtılar. [sentiment=Confident]',
    'vo_adrianavega_lazyriverland_bronze_060':
        'Yoo, ben giremem ki. Parkta bu kadar şey olurken- [sentiment=Shocked]',
    'vo_adrianavega_lostmonument_intro_080':
        'Aa, evet! Kesinlikle öyle. Özür dilerim, kimsenin gerçekten kim olduklarını bilmesine alışkın değilim... [sentiment=Shocked]',
    'vo_bradnewton_coastercanyon_intro_110':
        'Vay be, hiç baskı yok o zaman... Neyse, haydi başlayalım! [sentiment=Happy]',
    'vo_bradnewton_twinpeaks_outro_050':
        'Ha evet, ajan! Şimdi kendini bayağı aptal hissediyordur, değil mi Hank? [sentiment=Confident]',
    'vo_bradnewton_vomitworld_bronze_010':
        'Vay canına, bu ziyaretçiler gerçekten adrenalin düşkünü! [sentiment=Happy]',
    'vo_eugenenewton_lazyriverland_intro_090':
        'Aa, emin misin? Peki... ben ne yapmalıyım o zaman? [sentiment=Fear]',
    'vo_eugenenewton_tutorial1_bronze_120':
        'Ah Oswald. Keşke insanlara bunu söylemekten vazgeçsen... her ne kadar bu kupa için biraz daha cilalayıcı almam gerektiğini hatırlatsa da. Son görüşümde biraz donuk görünüyordu. [sentiment=Neutral]',
    'vo_eugenenewton_tutorial1_bronze_240':
        'Ha, bir de binişi daha önce yaptığın gibi açmayı unutma. Ama aslında... (düşünür) bu onu B-G-Ç-Y-G-A yapar, değil mi? Hmm, pek akılda kalmıyor. [sentiment=Neutral]',
    'vo_eugenenewton_tutorial1_bronze_240_alt':
        'Ha, bir de binişi daha önce yaptığın gibi açmayı unutma. [sentiment=Neutral]',
    'vo_eugenenewton_tutorial1_bronze_240_alt3':
        'Ha, bir de binişi açmayı unutma! Aslında... (düşünür) bu onu B-G-Ç-Y-A yapar, değil mi? Hmm... pek akılda kalmıyor. [sentiment=Fear]',
    'vo_nanabetty_archipelago_gold_070':
        'Ha, (masum bir kıkırdamayla) evet, ben de aynı şeyi söylüyordum... ama gitmem lazım- [sentiment=Happy]',
    'vo_nanabetty_chapter4_010':
        'Ah canlarım, şimdiye kadar başardıklarınız olağanüstü! Ve şimdi Nana Betty ailesine katılmanın eşiğindesiniz. [sentiment=Happy]',
    'vo_nanabetty_gardenpark_gold_050':
        'Ha, evet. (Kıkırdar) Hepinizin ne kadar güzel iş çıkardığını söylüyordum. [sentiment=Happy]',
    'vo_nanabetty_gardenpark_outro_090':
        'Aa, (Beceriksiz Kahkaha) sadece küçük bir iç espri, hepsi bu. Aa, ne şeytan misin! (Kıkırdar) [sentiment=Confused]',
    'vo_nanabetty_planningpermissionfailure_gold_090':
        'Aa, teşekkür ederim canım, çok naziksin. [sentiment=Happy]',
    'vo_nanabetty_planningpermissionfailure_intro_090':
        'Ah, sık sık uğramaya çalışırım. Bu yerin kalbimde özel bir yeri var, gerçekten. [sentiment=Happy]',
    'vo_nanabetty_planningpermissionfailure_silver_060':
        'Aa (kıkırdar) öyle mi. Ah, yaşlı kadının gözlerini bağışlayın. Eskisi gibi göremiyorlar artık. [sentiment=Happy]',
    'vo_oswaldthompson_coastline_intro_110':
        'Aa, merak etmeyin. Dostlar arasında biraz borç ne ki? [sentiment=Happy]',
    'vo_oswaldthompson_duellingparks_gold_040':
        'Ah, zamanla yumuşar. Parmakları çıtlatmakla o öfke gitmez. Tek yapabileceğimiz, sandığı insanlar olmadığımızı göstermeye devam etmek. [sentiment=Neutral]',
    'vo_oswaldthompson_duellingparks_outro_050':
        "Vay, 'mükemmel' mi? Yüzüm kızarıyor! [sentiment=Happy]",
    'vo_oswaldthompson_duellingparks_silver_020':
        'Aa, hiçbir yere gitmiyoruz! Her zaman aynı fikirde olmasak da, yıllarımın bana öğrettiği şu: müşteri her zaman haklıdır. [sentiment=Confident]',
    'vo_oswaldthompson_epilogue_010':
        "Aa, iyi! Geldiniz! Hank'in paylaşmak istediği BÜYÜK bir haberi olduğundan hepinizi burada topladım! [sentiment=Neutral]",
    'vo_oswaldthompson_planningpermissionfailure_intro_080':
        'Aa, Nana Betty, ne büyük onur! Bugün bu tarafa ne getirdi sizi? [sentiment=Neutral]',
    'vo_oswaldthompson_planningpermissionfailure_intro_110':
        "Ah, iyiliğiniz eşsiz; ama kendinizi zahmet ettirmeyin. Her şey Coaster Coast'ta çözülür! [sentiment=Happy]",
    'vo_oswaldthompson_tutorial1_gold_240':
        'Ah, (kıkırdar) her seferinde yakalanıyor... [sentiment=Happy]',
    'vo_oswaldthompson_tutorial1_outro_150':
        'Vay canına, bu bir şaheser! Siz ikiniz muhteşem iş çıkardınız! Bu, gerçekten ışıkları hak eden bir hız treni; haydi bunu ilan etmek için bir Reklam hazırlayalım, di mi? Park Yönetimi menüsündeki Reklam sekmesine gidin; dünyaya parkın sunduklarını gösterelim! [sentiment=Happy]',
    'vo_oswaldthompson_tutorial1_silver_040':
        'Aman Eugene, her zaman mükemmelliyetçiliğe gerek yok. Şu an görevimiz, bu güzel Plankonyalılara ve temel ihtiyaçlarına bakmak. [sentiment=Confident]',
}

changed = 0
for k, v in FIX.items():
    if k not in strings:
        print(f'UYARI: {k} yok')
        continue
    old = strings[k]['translation']
    if old != v:
        strings[k]['translation'] = v
        changed += 1
        print(f'OK {k}')

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n{changed}/{len(FIX)} güncellendi. Yedek: {BAK}')
