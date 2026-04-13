# Çeviri Kalite Sistemi Implementation Planı

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Terminoloji tutarsızlıklarını gidermek, 147 "çekici" hatasını düzeltmek, CLAUDE.md + validate.py ile gelecekteki seansları güvence altına almak.

**Architecture:** Önce araçlar (glossary, STYLE_GUIDE, CLAUDE.md, validate.py), sonra mevcut çeviriler düzeltilir. validate.py TDD ile genişletilir; çeviri düzeltmeleri dosya gruplarına ayrılır.

**Tech Stack:** Python 3.12, pytest, JSON (iki format: yapılandırılmış `tr.json` + düz `*_translated.json`)

---

## Dosya Haritası

| Durum | Dosya | Sorumluluk |
|-------|-------|------------|
| Güncelle | `glossary.json` | Tüm onaylı terim çevirileri |
| Güncelle | `docs/STYLE_GUIDE.md` | Ton kuralları + yapılmaması gerekenler |
| Oluştur | `CLAUDE.md` | Her oturumda otomatik yüklenen çeviri kılavuzu |
| Güncelle | `tools/validate.py` | Yasaklı terim + argo uyarı kontrolü |
| Oluştur | `tests/test_validate_forbidden.py` | Yeni validate kuralları için testler |
| Düzelt | `translations/infopanel_b4_translated.json` | 33 "çekici" |
| Düzelt | `translations/infopanel_b5_translated.json` | 6 "çekici" |
| Düzelt | `translations/infopanel_b3_translated.json` | 4 "çekici" |
| Düzelt | `translations/infopanel_b1_translated.json` | 1 "çekici" |
| Düzelt | `translations/notification_translated.json` | 5 "çekici" |
| Düzelt | `translations/parkmanagement_b2_translated.json` | 4 "çekici" |
| Düzelt | `translations/parkmanagement_b3_translated.json` | 4 "çekici" |
| Düzelt | `translations/sandboxsettings_translated.json` | 4 "çekici" |
| Düzelt | `translations/tutorialscreen_b1a_translated.json` | 3 "çekici" |
| Düzelt | `translations/tutorialscreen_b2_translated.json` | 8 "çekici" |
| Düzelt | `translations/vo_translated_b2.json` | 1 "çekici" |
| Düzelt | `translations/guest_thought_b1_translated.json` | Argo düzeltme |
| Düzelt | `translations/guest_thought_b3_translated.json` | Argo düzeltme |
| Düzelt | `translations/Content0/tr.json` | 74 "çekici" (yapılandırılmış format) |
| Güncelle | `docs/superpowers/specs/2026-04-13-turkce-yama-design.md` | Czech → English US/UK |
| Güncelle | `C:\Users\veysi\.claude\projects\C--Users-veysi-Projeler-PlanetCoaster2TurkceYama\memory\feedback_guest_thoughts_turkish.md` | Eski "valla/yahu" kuralı tersine çevrilir |

---

## Task 1: Glossary Genişletme

**Files:**
- Modify: `glossary.json`

- [ ] **Adım 1: glossary.json'u oku ve mevcut yapıyı kavra**

`glossary.json` dosyasını oku. Mevcut format: `{"meta": {...}, "terms": {"Term": {"translation": "...", "note": "..."}}}`

- [ ] **Adım 2: Tüm yeni terimleri ekle**

`glossary.json` içindeki `"terms"` bloğuna şu terimleri ekle (mevcut terimler korunur):

```json
"Attraction": {
  "translation": "Aktivite",
  "note": "UI başlık ve kategori bağlamında 'Aktivite'; pazarlama/tanıtım metninde 'Heyecan'. 'Thrill' da 'Heyecan' olduğundan aynı metinde 'Aktivite' tercih edilir."
},
"Flat Ride": {
  "translation": "Sabit Eğlence Birimi",
  "note": "Dönme, sallanma, kule tipi mekanik platformlar."
},
"Dark Ride": {
  "translation": "Kapalı Eğlence Birimi",
  "note": "Kapalı ortamda anlatı temelli binişler."
},
"Water Ride": {
  "translation": "Su Eğlence Birimi",
  "note": "Su içeren binişler."
},
"Transport Ride": {
  "translation": "Ulaşım Birimi",
  "note": "Ziyaretçileri parkta farklı noktalara taşır."
},
"Go Kart": {
  "translation": "Go-Kart",
  "note": "Özel isim olarak korunur, Türkçeleştirilmez."
},
"Flying Theatre": {
  "translation": "Uçuş Tiyatrosu",
  "note": "Hava simülasyonlu sinema deneyimi."
},
"Spinning Ride": {
  "translation": "Dönen Eğlence Birimi"
},
"Swinging Ride": {
  "translation": "Salınan Eğlence Birimi"
},
"Tower Ride": {
  "translation": "Kule Eğlence Birimi"
},
"Wooden Coaster": {
  "translation": "Ahşap Hız Treni"
},
"Hybrid Coaster": {
  "translation": "Hibrit Hız Treni"
},
"Finance": {
  "translation": "Finans",
  "note": "Park mali yönetimi bölümü."
},
"Loan": {
  "translation": "Kredi",
  "note": "Bankadan alınan borç."
},
"Marketing": {
  "translation": "Pazarlama",
  "note": "Reklam kampanyaları."
},
"Research": {
  "translation": "Araştırma",
  "note": "Tech Tree araştırma sistemi."
},
"Maintenance": {
  "translation": "Bakım",
  "note": "Personelin yaptığı rutin bakım."
},
"Refurbishment": {
  "translation": "Yenileme",
  "note": "Eğlence birimini sıfırlayan kapsamlı bakım."
},
"Running Costs": {
  "translation": "İşletme Giderleri",
  "note": "Aylık sabit giderler."
},
"Breakdown": {
  "translation": "Arıza",
  "note": "Eğlence biriminin beklenmedik arızası."
},
"Inspection": {
  "translation": "Denetim"
},
"Infrastructure": {
  "translation": "Altyapı",
  "note": "Jeneratör, pompa, su sistemi gibi park alt yapısı."
},
"Aging": {
  "translation": "Eskiyen",
  "note": "Prestij düşüş aşaması."
},
"Classic": {
  "translation": "Klasik",
  "note": "Prestij bonus aşaması."
},
"Established": {
  "translation": "Yerleşik",
  "note": "Normal işletim aşaması."
},
"Resurging": {
  "translation": "Canlanıyor",
  "note": "Prestij yükseliş aşaması."
},
"Reputation": {
  "translation": "İtibar",
  "note": "Eğlence biriminin ziyaretçi çekme skoru."
},
"Condition": {
  "translation": "Durum",
  "note": "Eğlence biriminin fiziksel yıpranma durumu."
},
"Patrol Zone": {
  "translation": "Devriye Bölgesi",
  "note": "Personelin görev alanı."
},
"Training": {
  "translation": "Eğitim",
  "note": "Personel seviye geliştirme sistemi."
},
"Wage": {
  "translation": "Maaş"
},
"Morale": {
  "translation": "Moral",
  "note": "Personel memnuniyet skoru."
},
"Ride Attendant": {
  "translation": "Biniş Görevlisi",
  "note": "Eğlence birimi operatörü."
},
"Workload": {
  "translation": "İş Yükü"
},
"Happiness": {
  "translation": "Mutluluk",
  "note": "Ziyaretçinin genel memnuniyet skoru."
},
"Hunger": {
  "translation": "Açlık"
},
"Thirst": {
  "translation": "Susuzluk"
},
"Energy": {
  "translation": "Enerji",
  "note": "Yorgunluğun tersi."
},
"Toilet Need": {
  "translation": "Tuvalet İhtiyacı"
},
"Mood": {
  "translation": "Ruh Hali",
  "note": "Ziyaretçinin anlık duygusal durumu."
},
"Thought": {
  "translation": "Düşünce",
  "note": "guest_thought kategorisi — ziyaretçinin içinden geçen düşünceler."
},
"Nausea Tolerance": {
  "translation": "Bulantı Toleransı"
},
"Queue Tolerance": {
  "translation": "Sıra Bekleme Sabrı"
},
"Fear Tolerance": {
  "translation": "Korku Toleransı"
},
"Price Tolerance": {
  "translation": "Fiyat Toleransı"
},
"Scenario": {
  "translation": "Senaryo",
  "note": "Belirli hedefleri olan oyun modu."
},
"Planet Points": {
  "translation": "Planet Points",
  "note": "Oyun adından gelir, çevrilmez."
},
"Tech Tree": {
  "translation": "Araştırma Ağacı"
},
"Heatmap": {
  "translation": "Isı Haritası",
  "note": "Sorunları renklerle görselleştiren araç."
},
"Season Track": {
  "translation": "Sezon Takibi"
},
"Trigger Sequence": {
  "translation": "Olay Zinciri",
  "note": "Event tetikleme ve sıralama sistemi."
},
"Footprint": {
  "translation": "Zemin Alanı",
  "note": "Yapının kapladığı yer boyutları."
},
"Station": {
  "translation": "İstasyon",
  "note": "Eğlence biriminin biniş-iniş noktası."
},
"Track Element": {
  "translation": "Ray Elementi",
  "note": "Ray sistemi bağlantı parçaları."
}
```

- [ ] **Adım 3: JSON geçerliliğini kontrol et**

```bash
./venv/Scripts/python.exe -c "import json; json.load(open('glossary.json', encoding='utf-8')); print('OK')"
```

Beklenen: `OK`

- [ ] **Adım 4: Commit**

```bash
git add glossary.json
git commit -m "feat(glossary): add 45 new game-specific terms"
```

---

## Task 2: STYLE_GUIDE.md Güncelleme

**Files:**
- Modify: `docs/STYLE_GUIDE.md`

- [ ] **Adım 1: Mevcut STYLE_GUIDE.md sonuna şu bölümleri ekle**

```markdown
## Guest Thoughts ve Diyalog Tonu

Ziyaretçi düşünceleri ve diyaloglar birinci tekil şahısla, spontane ve samimi yazılır.
Yazılı Türkçe normlarına uyar — ağız/sokak argosundan uzak.

**Kullanılabilir:**
- Doğal ünlemler: "Vay be!", "Müthiş!", "Harika!", "İnanılmaz!", "Berbat!"
- Duygu ifadeleri: "Sabırsızlanıyorum", "Dayanamıyorum", "Mükemmeldi"

**Kullanılmaz:**
- Ağız sözcükleri: "valla", "yahu", "be" (cümle başı/sonu), "ya" (cümle sonu)
- Kaba argo: "pes artık", "yeter yahu"

**Örnekler:**
- ✅ "En sevdiğim eğlence birimine bineceğim, sabırsızlanıyorum!"
- ✅ "Bu kadar kuyruğa değmez, bir daha gelmem!"
- ❌ "Valla favorime bineceğim, dayanamıyorum yahu!"

## Yapılmaması Gerekenler

| Hata | Yanlış | Doğru |
|------|--------|-------|
| Birebir çeviri | "up, up and away" → "yukarı, yukarı ve uzaklara" | "göklere fırlatır" |
| Yanlış terim | "ride" → "çekici" | "Eğlence Birimi" |
| Aşırı resmi | "deneyiminizi başlatın" | "hadi başlayalım" |
| Aşırı argo | "valla harika bir gün" | "Harika bir gün!" |
| İngilizce yapı | "Bu çekici {StartTime} içinde Klasik olacak" | "Bu eğlence birimi {StartTime} sonra Klasik aşamasına geçer" |

## İçerik Tiplerine Göre Ton Rehberi

| İçerik tipi | Ton | Örnek |
|-------------|-----|-------|
| UI buton/etiket | Kısa, net, emir kipi | "Kaydet", "Oyna" |
| Tooltip | 1-2 cümle, samimi, 2. tekil | "Bakım maliyetini gösterir" |
| Ride açıklaması | Akıcı, heyecan verici pazarlama dili | "Nefes kesen bir macera seni bekliyor!" |
| Guest thought | Doğal yazılı konuşma, birinci tekil | "Muhteşemdi, bir daha bineceğim!" |
| Tutorial | Öğretici, sıcak, adım adım | "Şimdi bir eğlence birimi yerleştir." |
| Kariyer diyalogu | Doğal, karaktere özgü | Karakterin kişiliğine uygun |
```

- [ ] **Adım 2: Commit**

```bash
git add docs/STYLE_GUIDE.md
git commit -m "docs(style-guide): add guest thoughts tone + forbidden patterns"
```

---

## Task 3: CLAUDE.md Oluşturma

**Files:**
- Create: `CLAUDE.md`

- [ ] **Adım 1: Proje kök dizinine CLAUDE.md yaz**

```markdown
# Planet Coaster 2 Türkçe Yama — Claude Kılavuzu

## Çeviri Seansına Başlamadan Önce ZORUNLU

1. `glossary.json` dosyasını oku — tüm onaylı terimler burada
2. `docs/STYLE_GUIDE.md` dosyasını oku — ton ve üslup kuralları
3. Hangi içerik tipini çevirdiğini belirle (UI, tooltip, ride açıklaması, guest thought, tutorial)
4. O içerik tipinin ton kuralını STYLE_GUIDE'dan uygula

## Asla Yapma

- `ride` veya `attraction` için **"çekici"** kullanma → doğrusu "Eğlence Birimi" veya "Aktivite"
- Cümle yapısını İngilizceden birebir çevirme
- "valla", "yahu", "be" (cümle sonu), "ya" (cümle sonu) kullanma
- Glossary'de olmayan terimler için kullanıcıya sormadan çeviri üretme

## Şüpheye Düştüğünde

- Yeni terim gerekiyorsa → önce kullanıcıya sor, onay sonrası glossary.json'a ekle, sonra çevir
- "Attraction" bağlama göre seçilir:
  - UI başlık, kategori, tablo başlığı → **"Aktivite"**
  - Pazarlama, tanıtım, heyecan vurgulu metin → **"Heyecan"**
  - Aynı metinde "Thrill" da varsa her zaman → **"Aktivite"** (karışıklık önlenir)

## Validate

Çeviri yaptıktan sonra çalıştır:
```bash
./venv/Scripts/python.exe tools/validate.py
```
[HATA] çıktısı varsa düzelt. [UYARI] çıktısı için bilinçli karar ver.

## Deploy Yöntemi

Mod klasörü crash yapıyor — kullanılmaz. Build sonrası şu iki dosya değiştirilmeli:
- `Content0/Localised/English/UnitedStates/Loc.ovl`
- `Content0/Localised/English/UnitedKingdom/Loc.ovl`

Orijinaller `.bak` uzantısıyla yedekli.
```

- [ ] **Adım 2: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: add CLAUDE.md with mandatory translation checklist"
```

---

## Task 4: validate.py — Yasaklı Terim ve Argo Kontrolü (TDD)

**Files:**
- Modify: `tools/validate.py`
- Create: `tests/test_validate_forbidden.py`

- [ ] **Adım 1: Önce failing testleri yaz**

`tests/test_validate_forbidden.py` dosyasını oluştur:

```python
"""validate.py yasaklı terim ve argo kontrolleri için testler."""
from tools.validate import check_forbidden_terms, check_colloquial_terms


def test_forbidden_term_cekici_detected():
    errors = check_forbidden_terms("ride_title", "Bu çekici çok hızlı")
    assert len(errors) == 1
    assert "çekici" in errors[0]
    assert "Eğlence Birimi" in errors[0]


def test_forbidden_term_case_insensitive():
    errors = check_forbidden_terms("ride_title", "Bu Çekici açıldığında")
    assert len(errors) == 1


def test_forbidden_term_clean_translation():
    errors = check_forbidden_terms("ride_title", "Bu eğlence birimi çok hızlı")
    assert errors == []


def test_forbidden_misafir_detected():
    errors = check_forbidden_terms("guest_label", "Misafir sayısı: 5")
    assert len(errors) == 1
    assert "misafir" in errors[0].lower()
    assert "Ziyaretçi" in errors[0]


def test_colloquial_valla_detected():
    warnings = check_colloquial_terms("guest_thought_1", "Valla harika bir gün!")
    assert len(warnings) == 1
    assert "valla" in warnings[0]


def test_colloquial_yahu_detected():
    warnings = check_colloquial_terms("guest_thought_2", "Yeter yahu bu kuyruk!")
    assert len(warnings) == 1
    assert "yahu" in warnings[0]


def test_colloquial_clean():
    warnings = check_colloquial_terms("guest_thought_3", "Harika bir gün geçirdim!")
    assert warnings == []


def test_colloquial_multiple_terms():
    warnings = check_colloquial_terms("x", "Valla yahu çok güzel!")
    assert len(warnings) == 2
```

- [ ] **Adım 2: Testlerin başarısız olduğunu doğrula**

```bash
./venv/Scripts/python.exe -m pytest tests/test_validate_forbidden.py -v 2>&1 | head -20
```

Beklenen: `ImportError` veya `AttributeError: module has no attribute 'check_forbidden_terms'`

- [ ] **Adım 3: validate.py'ye sabitler ve iki yeni fonksiyon ekle**

`tools/validate.py` dosyasında `PLACEHOLDER_PATTERNS` listesinin hemen altına şunu ekle:

```python
# Çeviride kesinlikle kullanılmaması gereken terimler → [HATA]
FORBIDDEN_TERMS: dict[str, str] = {
    "çekici": "Eğlence Birimi veya Aktivite",
    "misafir": "Ziyaretçi",
    "lunapark treni": "Hız Treni",
}

# Yazılı Türkçede kullanılmaması gereken ağız/argo sözcükler → [UYARI]
COLLOQUIAL_TERMS: list[str] = [
    "valla",
    "yahu",
    "pes artık",
    "yeter yahu",
]
```

`check_placeholders` fonksiyonunun hemen ardına (satır ~77 civarı) şu iki fonksiyonu ekle:

```python
def check_forbidden_terms(key: str, translation: str) -> list[str]:
    """Çeviride yasaklı terimlerin kullanılıp kullanılmadığını kontrol et.

    Returns: Hata mesajı listesi (boş = temiz).
    """
    errors: list[str] = []
    translation_lower = translation.lower()
    for term, suggestion in FORBIDDEN_TERMS.items():
        if term.lower() in translation_lower:
            errors.append(
                f"{key}: yasaklı terim '{term}' — kullan: '{suggestion}'"
            )
    return errors


def check_colloquial_terms(key: str, translation: str) -> list[str]:
    """Çeviride argo/ağız sözcüklerini tespit et.

    Returns: Uyarı mesajı listesi (boş = temiz). Uyarı = hata değil.
    """
    warnings: list[str] = []
    translation_lower = translation.lower()
    for term in COLLOQUIAL_TERMS:
        if term.lower() in translation_lower:
            warnings.append(
                f"{key}: argo/ağız sözcüğü '{term}' — yazılı Türkçede kullanılmaz"
            )
    return warnings
```

- [ ] **Adım 4: main() fonksiyonunu güncelle**

`main()` içinde `all_errors: list[str] = []` satırının hemen altına ekle:

```python
all_warnings: list[str] = []
```

Mevcut placeholder kontrol bloğunu şu şekilde genişlet:

```python
if not schema_errors and not args.check_glossary:
    data = json.loads(jf.read_text(encoding="utf-8"))
    for key, entry in data.get("strings", {}).items():
        if entry.get("translation"):
            ph_errors = check_placeholders(
                key, entry["source"], entry["translation"]
            )
            all_errors.extend(f"{jf}: {e}" for e in ph_errors)

            fb_errors = check_forbidden_terms(key, entry["translation"])
            all_errors.extend(f"[HATA]   {jf}: {e}" for e in fb_errors)

            cq_warnings = check_colloquial_terms(key, entry["translation"])
            all_warnings.extend(f"[UYARI]  {jf}: {w}" for w in cq_warnings)
```

`main()` sonundaki çıktı bloğunu şu şekilde değiştir (mevcut `if all_errors:` bloğunu bul, tümünü değiştir):

```python
    if all_warnings:
        for w in all_warnings:
            print(w)

    if all_errors:
        for err in all_errors:
            print(err, file=sys.stderr)
        print(f"\n{len(all_errors)} hata bulundu", file=sys.stderr)
        return 1

    msg = f"Tüm çeviriler geçerli ({len(json_files)} dosya kontrol edildi)"
    if all_warnings:
        msg += f" — {len(all_warnings)} uyarı (argo sözcük)"
    print(msg)
    return 0
```

- [ ] **Adım 5: Testleri çalıştır**

```bash
./venv/Scripts/python.exe -m pytest tests/ -v 2>&1 | tail -15
```

Beklenen: `15 passed` (eski) + `8 passed` (yeni) = **23 passed**

- [ ] **Adım 6: Commit**

```bash
git add tools/validate.py tests/test_validate_forbidden.py
git commit -m "feat(validate): add forbidden terms and colloquial term checks"
```

---

## Task 5: İnfopanel Flat Dosyalarını Düzelt

**Files:**
- Modify: `translations/infopanel_b4_translated.json`
- Modify: `translations/infopanel_b5_translated.json`
- Modify: `translations/infopanel_b3_translated.json`
- Modify: `translations/infopanel_b1_translated.json`

**Format notu:** Bu dosyalar düz `{"anahtar": "değer"}` formatındadır, `tr.json` yapılandırılmış formatından farklıdır.

**Değiştirme kuralı:**
- `"çekici"` (ride bağlamı, isim olarak) → `"eğlence birimi"`
- `"çekiciler"` (çoğul) → `"eğlence birimleri"`
- `"çekicinin"` → `"eğlence biriminin"`
- `"çekiciye"` → `"eğlence birimine"`
- `"çekiciyi"` → `"eğlence birimini"`
- `"çekicide"` → `"eğlence biriminde"`
- `"çekicideki"` → `"eğlence birimindeki"`
- `"Çekici"` (büyük harf, başlık) → `"Eğlence Birimi"`
- `"Çekiciler"` (çoğul başlık) → `"Eğlence Birimleri"`
- **DİKKAT:** `"çekicilik"` / `"çekiciliğini"` vb. → Bu kelimeler "attractiveness/appeal" anlamındadır, ride anlamında değil. Bağlamı oku; eğer "ziyaretçi çekiciliği / itibar" anlamındaysa `"cazibe"` veya `"çekicilik"` bırakılabilir ya da `"ziyaretçi çekim gücü"` kullanılabilir.

- [ ] **Adım 1: infopanel_b4_translated.json'u oku (33 "çekici")**

Dosyayı oku. Her "çekici" içeren değeri tespit et ve yukarıdaki kurala göre düzelt.

`infopanel_ride_*` prefixi: tümü "ride" bağlamı → "Eğlence Birimi"
`infopanel_ridephotos_*` prefixi: "ride photo" bağlamı → "Eğlence Birimi"
`infopanel_swimsuitrides`: "Mayo ile Binilen Çekiciler" → "Mayo ile Binilen Eğlence Birimleri"
`infopanel_transportrides`: "Ulaşım Çekicileri" → "Ulaşım Birimleri"
`infopanel_title_rideprestige`: "Çekici İtibarı" → "Eğlence Birimi İtibarı"
`infopanel_track_*`: "Çekici açıkken..." → "Eğlence birimi açıkken..."

`infopanel_ride_reputationdesc` özel durum — "İtibar, bir çekicinin Ziyaretçilere olan Çekiciliğini etkileyebilir." cümlesi hem ride hem appeal kullanıyor. Şu şekilde düzelt:
`"İtibar, bir eğlence biriminin ziyaretçiler üzerindeki etkisini belirler. Eğlence biriminin Prestijine bağlı olarak itibar durumu her an değişebilir."`

- [ ] **Adım 2: infopanel_b5_translated.json'u oku ve düzelt (6 "çekici")**

Dosyayı oku. Aynı kuralla tüm "çekici" → "eğlence birimi" değiştir.

- [ ] **Adım 3: infopanel_b3_translated.json'u oku ve düzelt (4 "çekici")**

Dosyayı oku. Aynı kuralla düzelt.

- [ ] **Adım 4: infopanel_b1_translated.json'u oku ve düzelt (1 "çekici")**

Dosyayı oku. Tek "çekici" kullanımını bul ve düzelt.

- [ ] **Adım 5: Değişiklikleri kontrol et**

```bash
grep -i "çekici" translations/infopanel_b1_translated.json translations/infopanel_b3_translated.json translations/infopanel_b4_translated.json translations/infopanel_b5_translated.json
```

Beklenen: Ride bağlamında sıfır sonuç. (`çekicilik` / `çekiciliği` gibi "appeal" anlamındaki kullanımlar kalabilir.)

- [ ] **Adım 6: Commit**

```bash
git add translations/infopanel_b1_translated.json translations/infopanel_b3_translated.json translations/infopanel_b4_translated.json translations/infopanel_b5_translated.json
git commit -m "fix(infopanel): replace 'çekici' with 'eğlence birimi' (44 occurrences)"
```

---

## Task 6: Diğer Flat Dosyaları Düzelt

**Files:**
- Modify: `translations/notification_translated.json` (5)
- Modify: `translations/parkmanagement_b2_translated.json` (4)
- Modify: `translations/parkmanagement_b3_translated.json` (4)
- Modify: `translations/sandboxsettings_translated.json` (4)
- Modify: `translations/tutorialscreen_b1a_translated.json` (3)
- Modify: `translations/tutorialscreen_b2_translated.json` (8)
- Modify: `translations/vo_translated_b2.json` (1)

- [ ] **Adım 1: Her dosyayı oku ve düzelt**

Her dosyada "çekici" içeren satırları bul. Bağlama göre:
- `notification_*`: Park bildirimleri — "ride" bağlamı → "Eğlence Birimi"
  - Örnek: "Ziyaretçiler çekicilere uzun yürüyor" → "Ziyaretçiler eğlence birimlerine uzun yürüyor"
- `parkmanagement_*`: Yönetim paneli — "ride" bağlamı → "Eğlence Birimi"
- `sandboxsettings_*`: Sandbox ayarları — bağlama göre düzelt
- `tutorialscreen_*`: Tutorial metinleri — "ride" bağlamı → "Eğlence Birimi"
- `vo_translated_b2.json`: Sesli anlatım metni — bağlamı oku, düzelt

- [ ] **Adım 2: Kontrol et**

```bash
grep -i "çekici" translations/notification_translated.json translations/parkmanagement_b2_translated.json translations/parkmanagement_b3_translated.json translations/sandboxsettings_translated.json translations/tutorialscreen_b1a_translated.json translations/tutorialscreen_b2_translated.json translations/vo_translated_b2.json
```

Beklenen: Ride bağlamında sıfır sonuç.

- [ ] **Adım 3: Commit**

```bash
git add translations/notification_translated.json translations/parkmanagement_b2_translated.json translations/parkmanagement_b3_translated.json translations/sandboxsettings_translated.json translations/tutorialscreen_b1a_translated.json translations/tutorialscreen_b2_translated.json translations/vo_translated_b2.json
git commit -m "fix(translations): replace 'çekici' in notification, parkmanagement, tutorialscreen (24 occurrences)"
```

---

## Task 7: Content0/tr.json — 74 "çekici" Düzeltme

**Files:**
- Modify: `translations/Content0/tr.json`

**Format notu:** Bu dosya yapılandırılmış formattadır (`"strings": {"key": {"source": "...", "translation": "...", "status": "..."}, ...}`). 74 "çekici" occurrence vardır ve dosya çok büyüktür (~28K string). Grep ile etkilenen satırları tespit et, her birini bağlamına göre düzelt.

- [ ] **Adım 1: Etkilenen key'leri tespit et**

```bash
grep -n '"çekici\|Çekici' translations/Content0/tr.json | head -80
```

Sonuçları incele. Her satırdaki key'i ve bağlamını anla.

- [ ] **Adım 2: Bağlam gruplarına ayır**

Key prefix'lerine göre gruplama:
- `infopanel_ride_*` → "ride" bağlamı → "Eğlence Birimi"
- `infopanel_affordableactivities*` → "çekiciler" → "eğlence birimleri"
- `infopanel_ridesandattractions` → "Rides and Attractions" → "Eğlence Birimleri ve Aktiviteler"
- `infopanel_attractionsincome/profit` → "Attractions Income/Profit" → "Aktivite Geliri/Kârı"

- [ ] **Adım 3: Düzeltmeleri uygula**

Her etkilenen string'i oku ve yukarıdaki değiştirme kurallarını uygula. Yapılandırılmış formatta sadece `"translation"` alanını değiştir; `"source"`, `"status"`, `"context"` alanlarına dokunma.

Özel durum — `infopanel_ride_reputationdesc` şu şekilde olmalı:
```json
"translation": "İtibar, bir eğlence biriminin ziyaretçiler üzerindeki etkisini belirler. Eğlence biriminin Prestijine bağlı olarak itibar durumu her an değişebilir."
```

- [ ] **Adım 4: validate.py çalıştır**

```bash
./venv/Scripts/python.exe tools/validate.py
```

`[HATA]` çıktısı: sıfır olmalı.
`[UYARI]` çıktısı: argo uyarıları olabilir — Task 9'da düzeltilecek.

- [ ] **Adım 5: Commit**

```bash
git add translations/Content0/tr.json
git commit -m "fix(Content0): replace 'çekici' with correct terms (74 occurrences)"
```

---

## Task 8: Guest Thought Argo Düzeltmeleri

**Files:**
- Modify: `translations/guest_thought_b1_translated.json`
- Modify: `translations/guest_thought_b3_translated.json`

- [ ] **Adım 1: guest_thought_b1_translated.json'da argo sözcükleri tespit et**

```bash
grep -i "valla\|yahu\|pes artık\|yeter yahu" translations/guest_thought_b1_translated.json
```

- [ ] **Adım 2: guest_thought_b3_translated.json'da argo sözcükleri tespit et**

```bash
grep -i "valla\|yahu\|pes artık\|yeter yahu" translations/guest_thought_b3_translated.json
```

- [ ] **Adım 3: Argo içeren satırları düzelt**

Her argo içeren düşünceyi STYLE_GUIDE kuralına göre yeniden yaz:
- "Valla favorime bineceğim!" → "En sevdiğim eğlence birimine bineceğim!"
- "Yeter yahu bu kuyruk!" → "Bu kadar kuyruğa değmez!"
- "Pes artık, ne rezalet!" → "Bu gerçekten berbat!"

Birinci tekil, spontane, yazılı Türkçe normlarında.

- [ ] **Adım 4: Kontrol et**

```bash
grep -i "valla\|yahu\|pes artık" translations/guest_thought_b1_translated.json translations/guest_thought_b3_translated.json
```

Beklenen: Sıfır sonuç.

- [ ] **Adım 5: Commit**

```bash
git add translations/guest_thought_b1_translated.json translations/guest_thought_b3_translated.json
git commit -m "fix(guest-thoughts): remove colloquial slang, use natural written Turkish"
```

---

## Task 9: Eski Tasarım Dokümanını Güncelle

**Files:**
- Modify: `docs/superpowers/specs/2026-04-13-turkce-yama-design.md`

- [ ] **Adım 1: Bölüm 7'yi (Dil Değiştirme Stratejisi) güncelle**

Şu değişiklikleri yap:
- "Neden Çekçe?" başlığı → "Neden English (US/UK)?" yap
- Eski Çekçe gerekçesini kaldır, şunu yaz: "Oyunun yerleşik Türkçe dil desteği bulunmadığından İngilizce (ABD ve İngiltere) dil dosyaları doğrudan değiştirilir. Mod klasörü yaklaşımı Xbox Game Pass sürümünde kararlılık sorununa yol açtığından bu yöntem benimsenmiştir."
- Mod yapısını güncelle:
  ```
  Content0/Localised/English/UnitedStates/Loc.ovl
  Content0/Localised/English/UnitedKingdom/Loc.ovl
  ```
- Manifest.xml / `Czech/CzechRepublic/Loc.ovl` referanslarını kaldır.

- [ ] **Adım 2: Commit**

```bash
git add docs/superpowers/specs/2026-04-13-turkce-yama-design.md
git commit -m "docs: update deploy method Czech -> English US/UK in design spec"
```

---

## Task 10: Bellek Güncelleme

**Files:**
- Modify: `C:\Users\veysi\.claude\projects\C--Users-veysi-Projeler-PlanetCoaster2TurkceYama\memory\feedback_guest_thoughts_turkish.md`
- Modify: `C:\Users\veysi\.claude\projects\C--Users-veysi-Projeler-PlanetCoaster2TurkceYama\memory\MEMORY.md`

- [ ] **Adım 1: feedback_guest_thoughts_turkish.md dosyasını güncelle**

Tüm içeriği şu şekilde değiştir:

```markdown
---
name: Ziyaretçi düşünceleri — doğal yazılı Türkçe, argo yok
description: guest_thought kategorisi samimi ama yazılı Türkçe normlarına uygun olmalı; "valla/yahu" gibi ağız sözcükleri kullanılmaz
type: feedback
---
Ziyaretçi düşünceleri (`guest_thought_*` kategorisi) birinci tekil şahısla, spontane ve samimi yazılır. Yazılı Türkçe normlarına uyar — ağız/sokak argosundan uzak.

**Why:** Başlangıçta "valla, yahu, be" gibi sokak argolarının Türk konuşma diline özgü olduğu düşünülerek kullanıldı. Kullanıcı bunları yazıya dökerken çok nadiren kullanıldığını ve tüm yaş gruplarına hitap eden bir oyun için uygunsuz olduğunu belirtti.

**How to apply:**
- Doğal ünlemler kullanılabilir: "Vay be!", "Müthiş!", "Harika!", "İnanılmaz!"
- Duygu ifadeleri: "Sabırsızlanıyorum", "Dayanamıyorum", "Mükemmeldi"
- KULLANILMAZ: "valla", "yahu", "be" (cümle başı/sonu), "ya" (cümle sonu), "pes artık", "yeter yahu"
- Olumlu: "En sevdiğim eğlence birimine bineceğim!" (❌ "Valla favorime bineceğim yahu!")
- Olumsuz: "Bu kadar kuyruğa değmez!" (❌ "Yeter yahu bu kuyruk!")
```

- [ ] **Adım 2: MEMORY.md'deki ilgili satırı güncelle**

`[Ziyaretçi düşünceleri Türklere özgü](feedback_guest_thoughts_turkish.md)` satırını şu şekilde değiştir:

```
- [Ziyaretçi düşünceleri — doğal yazılı Türkçe, argo yok](feedback_guest_thoughts_turkish.md) — guest_thought samimi ama yazılı normda; "valla/yahu" kullanılmaz
```

- [ ] **Adım 3: Son kontrol — tüm testler geçiyor mu?**

```bash
./venv/Scripts/python.exe -m pytest tests/ -v 2>&1 | tail -5
```

Beklenen: `23 passed`

- [ ] **Adım 4: validate.py son çalıştırma**

```bash
./venv/Scripts/python.exe tools/validate.py
```

`[HATA]` çıktısı: sıfır olmalı.

---

## Başarı Kriterleri

- [ ] `./venv/Scripts/python.exe -m pytest tests/ -v` → 23 passed, 0 failed
- [ ] `./venv/Scripts/python.exe tools/validate.py` → [HATA] sıfır
- [ ] `grep -ri "çekici" translations/ --include="*.json"` → ride bağlamında sıfır sonuç
- [ ] `grep -i "valla\|yahu\|pes artık" translations/guest_thought_*.json` → sıfır sonuç
- [ ] `CLAUDE.md` kök dizinde mevcut ve okunabilir
- [ ] `glossary.json` 45 yeni terim içeriyor
