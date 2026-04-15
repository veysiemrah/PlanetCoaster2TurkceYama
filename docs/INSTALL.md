# Kurulum Rehberi

## Kurulum (Windows)

1. [Releases](../../releases) sayfasından en son `TurkceYama-vX.Y.Z.zip` dosyasını indir
2. Zip'i boş bir klasöre çıkar — içinde hazır `TurkceYama/` klasörü, `kurulum.bat` ve `orijinal.bat` olacak
3. `kurulum.bat` dosyasına çift tıkla
4. Script oyun dizinini otomatik arar:
   - Xbox Game Pass: `C:\XboxGames`, `D:\XboxGames`, `E:\XboxGames`
   - Steam: `Program Files`, `Program Files (x86)`, `SteamLibrary`, `Steam` varyantları (C/D/E)
5. Otomatik bulamazsa kullanıcıdan `ovldata` dizini yolunu ister
6. Değiştirilecek dosyaların durumunu raporlar:
   - **Yedeği olmayan orijinal dosya**: `.bak` yedeği alınıp Türkçe ile değiştirilir
   - **Yedeği zaten olan dosya**: mevcut dosya silinip yenisi konur (yedek korunur)
   - **Hedef yok**: yeni konuma dosya kopyalanır
7. Onay (`E`) verdikten sonra kurulum tamamlanır
8. Oyunu başlat — Türkçe metinler aktif olur

## Manuel Kurulum

1. [Releases](../../releases) sayfasından `TurkceYama-vX.Y.Z.zip` dosyasını indir, çıkar
2. Oyun kurulum dizinini bul:
   - **Xbox Game Pass:** `C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata\`
   - **Steam:** `C:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata\`
3. Zip içinden çıkan `TurkceYama/Main/Content*/Localised/English/UnitedStates/Loc.ovl` dosyalarını oyun dizininde aynı konuma kopyala
4. Aynı `Loc.ovl` dosyasını `UnitedKingdom/Loc.ovl` olarak da kopyala
5. Orijinal İngilizce dosyaları önceden `.bak` uzantısıyla yedeklemeyi unutma
6. Oyunu başlat — Türkçe metinler aktif olur

## Nasıl Çalışır

Oyunda yerleşik Türkçe dil desteği bulunmadığından İngilizce (US/UK) dil dosyaları doğrudan Türkçe çeviri ile değiştirilir. Oyun İngilizce ile açıldığında metinler Türkçe görünür.

> Not: Önceki "mod klasörü" yöntemi Xbox Game Pass sürümünde oyunun çökmesine sebep olduğu için terk edilmiş; doğrudan dosya değiştirme yöntemi benimsenmiştir.

## Yamayı Kaldırma

### Otomatik (Önerilen)

`orijinal.bat` dosyasına çift tıkla:
- Oyun dizinini otomatik bulur
- Tüm `.bak` yedeklerini tarar ve raporlar
- Onay sonrası Türkçe dosyaları siler, orijinalleri `.bak`'tan geri yükler

### Manuel

1. `ovldata\Content*\Localised\English\UnitedStates\Loc.ovl` ve `UnitedKingdom\Loc.ovl` dosyalarını sil
2. Aynı klasörlerdeki `Loc.ovl.bak` dosyalarını `Loc.ovl` olarak yeniden adlandır
3. Oyunu başlat

### Yedek Yoksa

- **Steam:** "Dosya bütünlüğünü doğrula" (Verify integrity of game files) orijinal dosyaları geri yükler
- **Xbox Game Pass:** oyunu kaldırıp yeniden kurabilirsin

## Sorun Giderme

**Oyun açılmıyor**
Yedek `.bak` dosyalarını orijinal konuma geri taşı. Sorun devam ediyorsa oyun dosyalarını doğrula veya yeniden kur.

**Hâlâ çevrilmemiş görünüyor**
Oyunu tamamen kapatıp yeniden aç. Sorun devam ederse kurulumu doğrulayabilirsin: `ovldata\Content0\Localised\English\UnitedStates\Loc.ovl` dosyasının tarihine bak.

**Bazı metinler çevrilmemiş**
Çeviri devam ediyor. İlerleme için [README](../README.md) sayfasına bak.

**"Erişim engellendi" hatası**
`kurulum.bat` dosyasına sağ tıklayıp "Yönetici olarak çalıştır" seçeneğini kullan. Steam `Program Files` altında kurulu ise yönetici hakkı gerekebilir.

**Kurulum otomatik bulamıyor**
Oyununun kurulu olduğu `ovldata` klasörünün tam yolunu gir. Örnek:
```
D:\SteamLibrary\steamapps\common\Planet Coaster 2\Win64\ovldata
```
