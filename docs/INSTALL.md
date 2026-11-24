# Kurulum Rehberi

## Kurulum (Windows)

1. [PC2_TR_Yama.zip](https://github.com/veysiemrah/PlanetCoaster2TurkceYama/releases/latest/download/PC2_TR_Yama.zip) dosyasını indir
2. Zip'i boş bir klasöre çıkar — içinde hazır `TurkceYama/` klasörü, `kurulum.bat` ve `yama_sil.bat` olacak
3. `kurulum.bat` dosyasına çift tıkla
4. Script oyun dizinini otomatik arar:
   - Xbox Game Pass: `C:\XboxGames`, `D:\XboxGames`, `E:\XboxGames`
   - Steam: `Program Files`, `Program Files (x86)`, `SteamLibrary`, `Steam` varyantları (C/D/E)
   - Epic Games: Epic Launcher kayıtlarından gerçek kurulum yolu, ardından `Program Files\Epic Games` ve `Epic Games` klasörleri (C/D/E)
5. Otomatik bulamazsa kullanıcıdan `ovldata` dizini yolunu ister. Oyunun ana klasörü de girilebilir (örn. `D:\Oyunlar\PlanetCoaster2`); script `Win64\ovldata` kısmını kendisi bulur. Yolun tırnak içinde yapıştırılması da sorun değildir.
6. Değiştirilecek dosyaların durumunu raporlar:
   - **Yedeği olmayan orijinal dosya**: `.bak` yedeği alınıp Türkçe ile değiştirilir
   - **Yedeği zaten olan dosya**: mevcut dosya silinip yenisi konur (yedek korunur)
   - **Hedef yok**: yeni konuma dosya kopyalanır
7. Onay (`E`) verdikten sonra kurulum tamamlanır
8. Oyunu başlat — Türkçe metinler aktif olur

## Manuel Kurulum

1. [PC2_TR_Yama.zip](https://github.com/veysiemrah/PlanetCoaster2TurkceYama/releases/latest/download/PC2_TR_Yama.zip) dosyasını indir, çıkar
2. Oyun kurulum dizinini bul:
   - **Xbox Game Pass:** `C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata\`
   - **Steam:** `C:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata\`
   - **Epic Games:** `C:\Program Files\Epic Games\PlanetCoaster2\Win64\ovldata\` (Epic Launcher → Kütüphane → oyunun `...` menüsü → **Yönet** → klasör simgesi ile gerçek yolu görebilirsin)
3. Zip içinden çıkan `TurkceYama/Main/Content*/Localised/English/UnitedStates/Loc.ovl` dosyalarını oyun dizininde aynı konuma kopyala
4. Aynı `Loc.ovl` dosyasını `UnitedKingdom/Loc.ovl` olarak da kopyala
5. Orijinal İngilizce dosyaları önceden `.bak` uzantısıyla yedeklemeyi unutma
6. Oyunu başlat — Türkçe metinler aktif olur

## Nasıl Çalışır

Oyunda yerleşik Türkçe dil desteği bulunmadığından İngilizce (US/UK) dil dosyaları doğrudan Türkçe çeviri ile değiştirilir. Oyun İngilizce ile açıldığında metinler Türkçe görünür.

> Not: Önceki "mod klasörü" yöntemi Xbox Game Pass sürümünde oyunun çökmesine sebep olduğu için terk edilmiş; doğrudan dosya değiştirme yöntemi benimsenmiştir.

## Yamayı Kaldırma

### Otomatik (Önerilen)

`yama_sil.bat` dosyasına çift tıkla:
- Oyun dizinini otomatik bulur
- Tüm `.bak` yedeklerini tarar ve raporlar
- Onay sonrası **yalnızca yedeği (.bak) bulunan** dosyaları siler ve yedeklerden geri yükler
- Yedeği olmayan dosyalar korunur, silinmez

### Manuel

**Önce** her Content paketinin `.bak` dosyasının var olduğunu kontrol et. Yedeği olmayan Loc.ovl'i **silme** — aksi halde oyun bozulur.

1. `ovldata\Content*\Localised\English\UnitedStates\Loc.ovl.bak` dosyasının var olduğunu gör
2. Mevcut `Loc.ovl` dosyasını sil
3. `Loc.ovl.bak` dosyasını `Loc.ovl` olarak yeniden adlandır
4. `UnitedKingdom` için de aynı adımları tekrar et
5. Oyunu başlat

### Yedek Yoksa

Orijinal dosyaları geri almak için:
- **Steam:** "Dosya bütünlüğünü doğrula" (Verify integrity of game files)
- **Xbox Game Pass:** oyunu kaldırıp yeniden kurabilirsin
- **Epic Games:** Kütüphane → oyunun `...` menüsü → **Yönet** → **Doğrula**

## Sorun Giderme

**Oyun açılmıyor**
Yedek `.bak` dosyalarını orijinal konuma geri taşı. Sorun devam ediyorsa oyun dosyalarını doğrula veya yeniden kur.

**Hâlâ çevrilmemiş görünüyor**
Oyunu tamamen kapatıp yeniden aç. Sorun devam ederse kurulumu doğrulayabilirsin: `ovldata\Content0\Localised\English\UnitedStates\Loc.ovl` dosyasının tarihine bak.

**Bazı metinler çevrilmemiş**
Çeviri devam ediyor. İlerleme için [README](../README.md) sayfasına bak.

**"Erişim engellendi" / "Oyun klasörüne yazma izni yok" uyarısı**
Oyun `Program Files` gibi korumalı bir klasördeyse (Steam ve Epic'te sık görülür) yönetici hakkı gerekir. Script kopyalamadan önce yazma iznini kontrol eder; izin yoksa kendini yönetici olarak yeniden başlatmayı teklif eder. Açılan Windows izin penceresinde "Evet"e tıkla. İstersen baştan `kurulum.bat` dosyasına sağ tıklayıp "Yönetici olarak çalıştır" da diyebilirsin.

Kurulum sonunda "Başarısız işlem" sayısı 0 değilse script "Kurulum TAMAMLANAMADI" der: oyunu ve Steam/Epic'i kapatıp yönetici olarak tekrar çalıştır.

**Kurulum otomatik bulamıyor**
Oyununun kurulu olduğu `ovldata` klasörünün tam yolunu gir. Örnek:
```
D:\SteamLibrary\steamapps\common\Planet Coaster 2\Win64\ovldata
```
