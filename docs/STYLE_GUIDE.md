# Çeviri Stil Rehberi

Tüm çevirmenlerin uyması gereken kurallar.

## Hitap
Oyuncuya **"sen"** diye hitap edilir (samimi, senli-benli).
- ✅ "Parkına yeni bir tesis ekle"
- ❌ "Parkınıza yeni bir tesis ekleyiniz"

## Tutarlılık
Aynı İngilizce terim her yerde aynı Türkçe karşılıkla çevrilir.
- Referans: [`glossary.json`](../glossary.json)
- Yeni terim eklemek PR ile onaya tabidir.

## Doğallık
Birebir çeviri yerine Türkçede doğal akan ifadeler tercih edilir.
- ✅ "Park popülerliği artıyor"
- ❌ "Park popülaritesi artmaktadır"

## Kültürel Uyarlama
Para birimi, ölçü birimi gibi öğelerde oyun mantığı korunur. Oyunun kendi para birimi ("$") çevrilmez.

## Kısaltmalar
UI öğelerinde Türkçe uzadığında kabul edilebilir kısaltmalar kullanılabilir. `max_length` alanı varsa ona uyun.

## Değişkenler (Placeholder'lar)
`{0}`, `{1}`, `{name}`, `%s`, `%d` gibi placeholder'lar **asla** değiştirilmez. Çevirmen bunları korumak zorundadır.
- Source: `You earned {0} coins`
- ✅ Çeviri: `{0} jeton kazandın`
- ❌ Çeviri: `0 jeton kazandın` (placeholder kayboldu)

Formatlanmış değişkenler (`{Value:float:decimalPlaces=2}`) aynen korunur.

## Büyük/Küçük Harf
Başlıklar için her kelimenin baş harfi büyük (Türkçe başlık kuralı).

## Kategori Üslup Kuralları

| Kategori | Üslup | Örnek |
|----------|-------|-------|
| `ui_buttons` | Kısa, emir kipi | "Oyna", "Kaydet" |
| `ui_labels` | Kısa, isim | "Ayarlar", "Gelir" |
| `ui_tooltips` | Açıklayıcı, 2. tekil şahıs | "Parkına yeni bir tesis ekle" |
| `descriptions` | Detaylı, resmi | Tesis açıklamaları |
| `tutorials` | Öğretici, samimi | Eğitim metinleri |
| `career_dialogue` | Doğal, konuşma dili | Kariyer diyalogları |

## Türkçe Karakter
Her zaman tam Türkçe karakter kullanın: `ç ğ ı ö ş ü`. `c g i o s u` gibi ASCII karakter kullanmayın.
