# Planet Coaster 2 Türkçe Yama - Tasarım Dokümanı

**Tarih:** 2026-04-13
**Durum:** Onaylandı

---

## 1. Genel Bakış

Planet Coaster 2 için topluluk destekli, açık kaynaklı Türkçe çeviri yaması projesi. Oyunun Frontier Developments Cobra Engine (FRES/OVL format) dosyalarındaki metinleri Türkçeye çevirerek, Türkçe dil desteği olmayan oyuna Türkçe eklemeyi amaçlar.

### Hedefler
- Tüm oyun metinlerinin Türkçeleştirilmesi (menüler, açıklamalar, diyaloglar, DLC'ler dahil)
- Topluluk katılımına açık, GitHub tabanlı iş akışı
- Çeviri kalitesini ve tutarlılığı sağlayan otomasyon araçları
- Kolay kurulum ve dağıtım

### Kısıtlamalar
- Oyunda Türkçe dil seçeneği yok; mevcut bir dil (Çekçe) değiştirilecek
- OVL dosyaları binary formatta; cobra-tools ile extract/repack gerekiyor
- Xbox Game Pass, Steam ve diğer platformlarda çalışmalı

---

## 2. Oyun Dosya Yapısı

### Lokalizasyon Dosya Konumları
```
C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata\
├── Content_Localised/        # Küçük referans OVL dosyaları (~520 byte)
│   ├── Czech(CZ)/Localised/Czech/CzechRepublic/Loc.ovl
│   ├── English(GB)/Localised/English/UnitedKingdom/Loc.ovl
│   └── ... (diğer diller)
├── Content0/Localised/       # Ana çeviri dosyaları (~1.8 MB)
│   ├── Czech/CzechRepublic/Loc.ovl
│   ├── English/UnitedKingdom/Loc.ovl
│   └── ... (diğer diller)
├── Content1-8/Localised/     # Ek içerik çeviri dosyaları
├── ContentAnniversary/
├── ContentFestive/
└── ContentPDLC1-3/Localised/ # DLC çeviri dosyaları
```

### Dosya Formatı
- **Format:** FRES (Frontier Resource) / OVL arşiv
- **İçerik:** Her `Loc.ovl` içinde `.txt` dosyaları (dosya adı = string ID, içerik = çevrilmiş metin)
- **Sıkıştırma:** zlib
- **Hash:** DJB2

### Mevcut Diller
Czech, Dutch, English(GB), English(US), French, German, Italian, Japanese, Korean, Polish, Portuguese(BR), SimpleChinese, Spanish, TraditionalChinese

---

## 3. Proje Yapısı

```
PlanetCoaster2TurkceYama/
├── tools/                        # Python otomasyon scriptleri
│   ├── extract.py                # OVL -> JSON çıkartma
│   ├── build.py                  # JSON -> OVL paketleme
│   └── validate.py               # Çeviri doğrulama ve istatistik
├── translations/                 # Türkçe çeviri dosyaları (topluluk düzenler)
│   ├── Content0/tr.json
│   ├── Content1/tr.json
│   ├── ...
│   ├── ContentPDLC1/tr.json
│   └── ContentPDLC3/tr.json
├── source/                       # İngilizce kaynak metinler (referans, salt okunur)
│   ├── Content0/en.json
│   └── ...
├── glossary.json                 # Terimler sözlüğü
├── output/                       # Build çıktısı (.gitignore)
│   └── TurkceYama/
│       ├── Manifest.xml
│       └── Main/Localised/Czech/CzechRepublic/Loc.ovl
├── docs/
│   ├── STYLE_GUIDE.md            # Çeviri stil rehberi
│   ├── CONTRIBUTING.md           # Katkı rehberi
│   └── INSTALL.md                # Kurulum rehberi
├── .github/
│   └── workflows/
│       ├── validate.yml          # PR doğrulama CI
│       └── release.yml           # Otomatik build ve release
├── kurulum.bat                   # Windows kurulum scripti
├── README.md
└── requirements.txt              # Python bağımlılıkları (cobra-tools)
```

---

## 4. JSON Çeviri Formatı

```json
{
  "meta": {
    "language": "tr",
    "source_language": "en",
    "content_pack": "Content0",
    "game_version": "1.x.x",
    "last_updated": "2026-04-13"
  },
  "strings": {
    "UI_MainMenu_Play": {
      "source": "Play",
      "translation": "Oyna",
      "status": "translated",
      "context": "Ana menü başlat butonu",
      "max_length": null,
      "category": "ui_buttons"
    },
    "UI_MainMenu_Settings": {
      "source": "Settings",
      "translation": "",
      "status": "untranslated",
      "context": "Ana menü ayarlar butonu",
      "max_length": null,
      "category": "ui_buttons"
    }
  }
}
```

### String Alanları
| Alan | Zorunlu | Açıklama |
|------|---------|----------|
| `source` | Evet | İngilizce orijinal metin |
| `translation` | Evet | Türkçe çeviri (boş = çevrilmemiş) |
| `status` | Evet | `untranslated`, `translated`, `needs_review` |
| `context` | Hayır | String'in oyunda nerede kullanıldığı |
| `max_length` | Hayır | UI sığdırma için karakter limiti |
| `category` | Hayır | Fonksiyonel gruplama |

---

## 5. Kalite Kontrol Sistemi

### 5.1 Terimler Sözlüğü (`glossary.json`)

Oyuna özgü terimlerin tek bir onaylanmış çevirisi. Tüm çevirmenler buna uyar.

```json
{
  "terms": {
    "Coaster": {
      "translation": "Hız Treni",
      "note": "'Roller coaster' kısaltması. 'Lunapark treni' kullanılmaz."
    },
    "Guest": {
      "translation": "Ziyaretçi",
      "note": "Tema parkı bağlamı. 'Misafir' değil."
    },
    "Ride": {
      "translation": "Eğlence Birimi",
      "note": "Genel bir eğlence tesisi."
    },
    "Scenery": {
      "translation": "Dekorasyon",
      "note": "Park süsleme öğeleri."
    }
  }
}
```

Sözlüğe yeni terim eklemek PR ile yapılır ve reviewer onayına tabidir.

### 5.2 Kategori Sistemi ve Üslup Kuralları

| Kategori | Üslup | Örnek |
|----------|-------|-------|
| `ui_buttons` | Kısa, emir kipi | "Oyna", "Kaydet" |
| `ui_labels` | Kısa, isim | "Ayarlar", "Gelir" |
| `ui_tooltips` | Açıklayıcı, 2. tekil şahıs | "Parkına yeni bir tesis ekle" |
| `descriptions` | Detaylı, resmi | Tesis açıklamaları |
| `tutorials` | Öğretici, samimi | Eğitim metinleri |
| `career_dialogue` | Doğal, konuşma dili | Kariyer modu diyalogları |

### 5.3 Çeviri Stil Rehberi (Temel Kurallar)

- **Hitap:** Oyuncuya "sen" diye hitap (samimi, senli-benli)
- **Tutarlılık:** Aynı İngilizce terim her yerde aynı Türkçe karşılıkla çevrilir (glossary.json'a uygun)
- **Doğallık:** Birebir çeviri yerine Türkçede doğal akan ifadeler tercih edilir
- **Kültürel uyarlama:** Para birimi, ölçü birimi gibi öğelerde oyun mantığı korunur
- **Kısaltmalar:** UI öğelerinde Türkçe uzadığında kabul edilebilir kısaltmalar kullanılabilir
- **Değişkenler:** `{0}`, `{1}` gibi placeholder'lar asla değiştirilmez
- **Büyük/küçük harf:** Başlıklar için her kelimenin baş harfi büyük (Türkçe başlık kuralı)

### 5.4 Otomatik Doğrulama (`validate.py`)

PR'larda ve build sırasında çalışan kontroller:

1. **Sözlük tutarlılığı:** Glossary'deki terimlerin doğru kullanılıp kullanılmadığı
2. **Eksik çeviri:** Boş translation alanı olan string'ler
3. **Karakter limiti:** `max_length` aşılmış mı
4. **Placeholder koruma:** `{0}`, `{1}`, `%s`, `%d` gibi değişkenlerin korunması
5. **Duplikasyon kontrolü:** Aynı source string'in farklı şekillerde çevrilmesi
6. **Format hatası:** JSON syntax hataları
7. **İstatistik raporu:** Çeviri ilerleme yüzdesi

### 5.5 PR İnceleme Süreci

```
Çevirmen fork eder
    -> translations/ altında JSON düzenler
    -> PR açar
    -> GitHub Actions: validate.py otomatik çalışır
    -> En az 1 reviewer onaylar
    -> Merge edilir
```

---

## 6. Araçlar (tools/)

### 6.1 extract.py
- cobra-tools `LocalizationManager` API'si ile OVL dosyalarını açar
- Her Content paketi için ayrı `en.json` oluşturur
- Bağlam bilgisini otomatik çıkarır (dosya adı, yol, kategori tahmini)
- Kullanım: `python tools/extract.py --game-dir "C:\XboxGames\Planet Coaster 2"`

### 6.2 build.py
- `translations/` altındaki `tr.json` dosyalarını okur
- cobra-tools ile `Loc.ovl` dosyaları oluşturur
- Mod dizin yapısını hazırlar (Manifest.xml dahil)
- Kullanım: `python tools/build.py --output output/`

### 6.3 validate.py
- JSON doğrulama, sözlük kontrolü, istatistik
- CI ve lokal kullanım için
- Kullanım:
  - `python tools/validate.py` — tam doğrulama
  - `python tools/validate.py --stats` — ilerleme istatistiği
  - `python tools/validate.py --check-glossary` — sadece sözlük kontrolü

---

## 7. Dil Değiştirme Stratejisi

Oyunda Türkçe dil seçeneği olmadığından **İngilizce (US ve UK)** dil dosyaları doğrudan değiştirilir.

### Neden English (US/UK)?
- Mod klasörü yaklaşımı (Manifest.xml) Xbox Game Pass sürümünde kararlılık sorunu yarattığından bu yöntem benimsenmiştir.
- İngilizce dil dosyalarını değiştirmek en geniş kullanıcı kitlesine hitap eder.
- Kurulum: Oyun ayarlarından dil **"English (United States)"** olarak seçilir → Türkçe görünür.

### Deploy Yöntemi
Build sonrası şu iki dosya oyun dizininde yerine kopyalanır:

```
Content0/Localised/English/UnitedStates/Loc.ovl
Content0/Localised/English/UnitedKingdom/Loc.ovl
```

Orijinal dosyalar `.bak` uzantısıyla yedeklenir. Oyun güncellemesinin ardından build + kopyalama tekrarlanır.

---

## 8. Dağıtım ve Kurulum

### 8.1 GitHub Releases
- `main` branch'e merge yapıldığında GitHub Actions otomatik build yapar
- Release'e hazır yama dosyaları (zip) eklenir
- Kullanıcılar sadece Release'den indirir

### 8.2 Kurulum Scripti (`kurulum.bat`)
1. Oyun dizinini otomatik bul:
   - Xbox Game Pass ve Steam için C/D/E sürücülerini tarar
   - Steam varyantları: `Program Files`, `Program Files (x86)`, `SteamLibrary`, `Steam`
2. Bulunamazsa kullanıcıdan `ovldata` yolunu ister
3. Tüm `Content*` paketlerinde hedef dosyaların yedek durumunu tarar
4. Kullanıcıya yapılacak işlemleri rapor eder (yedek alınacak / değiştirilecek / yeni konum)
5. Onay (`E`) sonrası:
   - Yedeği olmayan orijinal `Loc.ovl` dosyaları `.bak` olarak yedeklenir
   - Türkçe `Loc.ovl` dosyaları `UnitedStates` ve `UnitedKingdom` altına kopyalanır
6. Özet rapor ve başarılı kurulum mesajı gösterir

### 8.3 Manuel Kurulum
1. Release'den zip indir
2. `Loc.ovl` dosyalarını ilgili dizinlere kopyala
3. Oyunda dili **"English (United States)"** olarak değiştir

---

## 9. GitHub Actions CI/CD

### validate.yml (PR'larda)
- `validate.py` çalıştırır
- JSON format kontrolü
- Sözlük tutarlılığı
- Placeholder koruma kontrolü

### release.yml (main branch merge)
- `build.py` çalıştırır
- Loc.ovl dosyaları oluşturur
- Zip olarak paketler
- GitHub Release oluşturur
- README'deki ilerleme istatistiklerini günceller

---

## 10. İlerleme Takibi

`validate.py --stats` çıktısı:
```
Content0:           1847/5200  (%35.5) çevrildi
Content1:              0/320   (%0.0)  çevrildi
ContentPDLC1:          0/450   (%0.0)  çevrildi
────────────────────────────────────────────────
Toplam:             1847/8500  (%21.7) çevrildi
```

Bu istatistik README.md'de otomatik güncellenir (CI ile).

---

## 11. Bağımlılıklar

- **Python 3.10+**
- **cobra-tools** (GitHub: OpenNaja/cobra-tools) — OVL extract/repack
- **GitHub Actions** — CI/CD

---

## 12. Riskler ve Azaltma

| Risk | Etki | Azaltma |
|------|------|---------|
| Oyun güncellemesi OVL formatını değiştirirse | Build kırılır | cobra-tools'u takip et, hızla güncelle |
| cobra-tools PC2 desteğini bırakırsa | Extract/build çalışmayı durdurur | Fork al, gerekirse özel parser yaz |
| Çekçe dili yerine başka dil tercih edilirse | Kurulum rehberi değişir | Build scriptinde dil parametrik, kolayca değiştirilebilir |
| Xbox Game Pass dosya erişim kısıtlamaları | Extract yapılamaz | Farklı platform kullanıcıları için alternatif yollar dokümente et |
