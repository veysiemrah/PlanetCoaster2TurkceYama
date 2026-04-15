# Planet Coaster 2 Türkçe Yama

[![Son Sürüm](https://img.shields.io/github/v/release/veysiemrah/PlanetCoaster2TurkceYama?label=son%20sürüm)](https://github.com/veysiemrah/PlanetCoaster2TurkceYama/releases/latest)
[![İndirme](https://img.shields.io/github/downloads/veysiemrah/PlanetCoaster2TurkceYama/total?label=toplam%20indirme)](https://github.com/veysiemrah/PlanetCoaster2TurkceYama/releases)
[![Lisans](https://img.shields.io/github/license/veysiemrah/PlanetCoaster2TurkceYama)](LICENSE)

📦 **[En son sürümü indir (PC2_TR_Yama.zip)](https://github.com/veysiemrah/PlanetCoaster2TurkceYama/releases/latest/download/PC2_TR_Yama.zip)**

## Durum

**✅ Tamamlandı — %100 çeviri** (32.665/32.665 string)

Tüm 14 içerik paketi çevrildi:
- **Content0** — Ana oyun (28.994)
- **Content1-8** — Oyun içi içerik (2.278)
- **ContentAnniversary, ContentFestive** — Tematik etkinlikler (372)
- **ContentPDLC1-3** — DLC paketleri (1.020)

## Kurulum

1. [PC2_TR_Yama.zip](https://github.com/veysiemrah/PlanetCoaster2TurkceYama/releases/latest/download/PC2_TR_Yama.zip) dosyasını indir
2. Zip'i boş bir klasöre çıkar
3. `kurulum.bat` dosyasına çift tıkla
4. Oyunu başlat — Türkçe metinler aktif olur

Yamayı kaldırmak için aynı klasördeki `orijinal.bat` dosyasını çalıştır.

Detaylı kurulum kılavuzu: [docs/INSTALL.md](docs/INSTALL.md)

## Nasıl Çalışır

Oyunda yerleşik Türkçe dil desteği bulunmadığından İngilizce (US/UK) dil dosyaları Türkçe çeviri ile değiştirilir. Oyun İngilizce ile açıldığında Türkçe metinler görünür.

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

Bir çeviriye katkıda bulunmadan önce [glossary.json](glossary.json) ve [docs/STYLE_GUIDE.md](docs/STYLE_GUIDE.md) dosyalarını okuyunuz lütfen.

## Teknik Detaylar

- **Dil**: Python 3.12+
- **Bağımlılıklar**: `requirements.txt` (cobra-tools için)
- **Validasyon**: `python tools/validate.py`
- **Build**: `python tools/build.py --game-dir "<oyun-dizini>"`
- **Release**: `.\tools\release.ps1 -Version v1.0.0` (build + zip + `gh release upload`)

## Lisans

[MIT](LICENSE)

## Teşekkürler

- [cobra-tools](https://github.com/OpenNaja/cobra-tools) — OVL dosya format desteği
- Planet Coaster 2 topluluğu — geri bildirim ve testler
