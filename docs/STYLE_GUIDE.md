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
