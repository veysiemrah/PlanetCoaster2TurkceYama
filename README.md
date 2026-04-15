# Planet Coaster 2 Türkçe Yama

## Durum

**✅ Tamamlandı — %100 çeviri** (32.665/32.665 string)

Tüm 14 içerik paketi çevrildi:
- **Content0** — Ana oyun (28.994)
- **Content1-8** — Oyun içi içerik (2.278)
- **ContentAnniversary, ContentFestive** — Tematik etkinlikler (372)
- **ContentPDLC1-3** — DLC paketleri (1.020)

## Kurulum

### Otomatik (Önerilen)

1. [Releases](../../releases) sayfasından en son `TurkceYama-vX.Y.Z.zip` dosyasını indir
2. Zip'i boş bir klasöre çıkar
3. `kurulum.bat` dosyasına çift tıkla
4. Script otomatik olarak oyun dizinini bulur, orijinal dosyaları yedekler ve Türkçe yamayı kurar
5. Oyunu başlat, **Ayarlar > Dil** menüsünden **English (United States)** veya **English (United Kingdom)** seç

Detaylı kurulum kılavuzu: [docs/INSTALL.md](docs/INSTALL.md)

## Dil Ayarı

Oyunda yerleşik Türkçe dil desteği bulunmadığından **English (US/UK)** dil dosyaları Türkçe çeviri ile değiştirilir. Oyun içinde dili "English (US)" veya "English (UK)" seçtiğinde Türkçe görürsün.

## Özellikler

- **Tam çeviri**: Oyun arayüzü, eğitimler, ziyaretçi düşünceleri, VO diyalogları, DLC içerikleri
- **Tutarlı terminoloji**: 100+ terimlik resmi sözlük ([glossary.json](glossary.json))
- **Üslup rehberi**: İçerik tipine göre ton kuralları ([docs/STYLE_GUIDE.md](docs/STYLE_GUIDE.md))
- **Otomatik validasyon**: Placeholder koruması, glossary uyumu, argo filtresi

## Katkıda Bulunma

Çeviri önerisi, hata bildirimi veya iyileştirme yapmak istiyorsan:

- **Hata/öneri**: [GitHub Issues](../../issues) üzerinden bildir
- **Çeviri katkısı**: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
- **Geliştirici bilgisi**: [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)

Bir çeviriye katkıda bulunmadan önce [glossary.json](glossary.json) ve [docs/STYLE_GUIDE.md](docs/STYLE_GUIDE.md) dosyalarını okumanı rica ederiz.

## Teknik Detaylar

- **Dil**: Python 3.12+
- **Bağımlılıklar**: `requirements.txt` (cobra-tools için)
- **Validasyon**: `python tools/validate.py`
- **Build**: `python tools/build.py --game-dir "<oyun-dizini>"`

## Lisans

[MIT](LICENSE)

## Teşekkürler

- [cobra-tools](https://github.com/OpenNaja/cobra-tools) — OVL dosya format desteği
- Planet Coaster 2 topluluğu — geri bildirim ve testler
