# Planet Coaster 2 Türkçe Yama — Katkıcı Kılavuzu

Bu dosya hem insan katkıcılar hem de AI asistanları (Claude, Copilot vb.) için çeviri rehberidir.

## Çeviri Oturumuna Başlamadan Önce

1. `glossary.json` dosyasını oku — tüm onaylı terimler burada
2. `docs/STYLE_GUIDE.md` dosyasını oku — ton ve üslup kuralları
3. Hangi içerik tipini çevirdiğini belirle (UI, tooltip, ride açıklaması, guest thought, tutorial, marketing)
4. O içerik tipinin ton kuralını STYLE_GUIDE'dan uygula

## Temel Kurallar

### Asla yapma
- `ride` veya `attraction` için **"çekici"** kullanma — yanlış çağrışım yapar
- Cümle yapısını İngilizceden birebir çevirme — doğal Türkçe öncelikli
- "valla", "yahu", "be" (cümle sonu), "ya" (cümle sonu) gibi argo/konuşma dili kullanma
- Glossary'de olmayan yeni terimler için onay almadan çeviri üretme

### Temel terim seçimleri (glossary'den)
- **Ride** → **Tren** (coaster/track/rail bağlamında) veya **Araç** (flat ride / genel)
- **Coaster** → **Hız Treni**
- **Scenery** → **Dekor**
- **Thrill** → **Gerilim** (Excitement ile çakışmaması için)
- **Excitement** → **Heyecan**
- **Nausea** → **Bulantı**
- **Attraction** → **Aktivite** (UI/kategori) veya **Atraksiyon** (tutorial/uzun metin)
- **Appeal** → **Cazibe** (asla "Çekicilik" değil)

Compound terimler:
- Flat Ride → **Sabit Oyun**, Ride Attendant → **Biniş Görevlisi**
- Transport Ride → **Ulaşım Aracı**
- Spinning/Swinging/Tower Ride → **Dönen/Salınan/Kule Eğlence**
- Track Ride → **Raylı Eğlence**

## Şüpheye Düştüğünde

- Yeni terim gerekirse: önce tartış (issue aç), onay sonrası `glossary.json`'a ekle, sonra çevir
- Marketing vs UI bağlamı: UI'da kısa ve net, marketing'de akıcı ve çekici

## Çeviri Sonrası Validate

```bash
# Linux/Mac
python tools/validate.py

# Windows
.\venv\Scripts\python.exe tools/validate.py
```

`[HATA]` çıktısı varsa düzelt. `[UYARI]` çıktısı için bilinçli karar ver.

## Deploy Yöntemi

Mod klasörü yaklaşımı Xbox Game Pass sürümünde çökmeye sebep olduğu için kullanılmaz. Bunun yerine İngilizce (US/UK) Loc.ovl dosyaları doğrudan değiştirilir:

- `Content*/Localised/English/UnitedStates/Loc.ovl`
- `Content*/Localised/English/UnitedKingdom/Loc.ovl`

Orijinaller `.bak` uzantısıyla yedeklenir. `kurulum.bat` bu süreci otomatikleştirir.
