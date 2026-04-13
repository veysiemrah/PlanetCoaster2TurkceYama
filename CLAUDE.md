# Planet Coaster 2 Türkçe Yama — Claude Kılavuzu

## Çeviri Seansına Başlamadan Önce ZORUNLU

1. `glossary.json` dosyasını oku — tüm onaylı terimler burada
2. `docs/STYLE_GUIDE.md` dosyasını oku — ton ve üslup kuralları
3. Hangi içerik tipini çevirdiğini belirle (UI, tooltip, ride açıklaması, guest thought, tutorial)
4. O içerik tipinin ton kuralını STYLE_GUIDE'dan uygula

## Asla Yapma

- `ride` veya `attraction` için **"çekici"** kullanma — doğrusu "Eğlence Birimi" veya "Aktivite"
- Cümle yapısını İngilizceden birebir çevirme
- "valla", "yahu", "be" (cümle sonu), "ya" (cümle sonu) kullanma
- Glossary'de olmayan terimler için kullanıcıya sormadan çeviri üretme

## Şüpheye Düştüğünde

- Yeni terim gerekiyorsa: önce kullanıcıya sor, onay sonrası `glossary.json`'a ekle, sonra çevir
- "Attraction" bağlama göre seçilir:
  - UI başlık, kategori, tablo başlığı → **"Aktivite"**
  - Pazarlama, tanıtım, heyecan vurgulu metin → **"Heyecan"**
  - Aynı metinde "Thrill" da varsa her zaman → **"Aktivite"** (karışıklık önlenir)

## Çeviri Sonrası Validate

```bash
./venv/Scripts/python.exe tools/validate.py
```

`[HATA]` çıktısı varsa düzelt. `[UYARI]` çıktısı için bilinçli karar ver.

## Deploy Yöntemi

Mod klasörü crash yapıyor — kullanılmaz. Build sonrası şu iki dosya değiştirilmeli:

- `Content0/Localised/English/UnitedStates/Loc.ovl`
- `Content0/Localised/English/UnitedKingdom/Loc.ovl`

Orijinaller `.bak` uzantısıyla yedekli.
