# Planet Coaster 2 Türkçe Yama — Çeviri Kalite Sistemi Tasarımı

**Tarih:** 2026-04-14
**Durum:** Onaylandı

---

## 1. Genel Bakış

Mevcut çevirilerde tespit edilen sistematik kalite sorunlarını gidermek ve gelecekte aynı sorunların yaşanmamasını sağlamak için kapsamlı bir kalite sistemi. Temel sorunlar:

- "ride/attraction" → "çekici" hatası (147 yerde, 12 dosyada)
- Birebir/kelime-kelime çeviri kalıpları
- Glossary ihlalleri (terminoloji tutarsızlığı)
- Aşırı argo kullanımı (guest thoughts: "valla", "yahu" vb.)
- Glossary'de eksik oyun terimleri
- Projeye yeni oturumda başlarken otomatik kılavuz eksikliği

---

## 2. Kapsam

### Etkilenen Dosyalar (Düzeltme Gerekli)
```
translations/infopanel_b1_translated.json
translations/infopanel_b3_translated.json
translations/infopanel_b4_translated.json
translations/infopanel_b5_translated.json
translations/Content0/tr.json            (74 "çekici" + kalite sorunları)
translations/notification_translated.json
translations/parkmanagement_b2_translated.json
translations/parkmanagement_b3_translated.json
translations/sandboxsettings_translated.json
translations/tutorialscreen_b1a_translated.json
translations/tutorialscreen_b2_translated.json
translations/guest_thought_b1_translated.json
translations/guest_thought_b3_translated.json
```

### Güncellenecek Dokümanlar
```
glossary.json
docs/STYLE_GUIDE.md
docs/superpowers/specs/2026-04-13-turkce-yama-design.md  (Czech → English US/UK)
CLAUDE.md                                                  (yeni oluşturulacak)
tools/validate.py                                          (yeni kurallar)
memory/feedback_guest_thoughts_turkish.md                  (eski kural tersine çevrilecek)
```

---

## 3. Glossary Genişletme

### 3.1 Güncellenen Terimler

| İngilizce | Türkçe | Not |
|-----------|--------|-----|
| Ride | Eğlence Birimi | Mevcut, korunur |
| Attraction | Aktivite veya Heyecan | UI/başlık → "Aktivite"; pazarlama/tanıtım → "Heyecan". "Thrill" da "Heyecan" olduğu için aynı metinde dikkatli kullanılmalı |

### 3.2 Yeni Eklenen Terimler

#### Eğlence Birimi Tipleri
| İngilizce | Türkçe | Not |
|-----------|--------|-----|
| Flat Ride | Sabit Eğlence Birimi | Dönme, sallanma, kule tipi |
| Dark Ride | Kapalı Eğlence Birimi | Kapalı ortam, anlatı temelli |
| Water Ride | Su Eğlence Birimi | Su içeren binişler |
| Transport Ride | Ulaşım Birimi | Parkta yer değiştirme |
| Go Kart | Go-Kart | Özel isim olarak korunur |
| Flying Theatre | Uçuş Tiyatrosu | Hava simülasyonlu |
| Spinning Ride | Dönen Eğlence Birimi | |
| Swinging Ride | Salınan Eğlence Birimi | |
| Tower Ride | Kule Eğlence Birimi | |
| Wooden Coaster | Ahşap Hız Treni | |
| Hybrid Coaster | Hibrit Hız Treni | |

#### Park Yönetimi
| İngilizce | Türkçe | Not |
|-----------|--------|-----|
| Finance | Finans | |
| Loan | Kredi | |
| Marketing | Pazarlama | |
| Research | Araştırma | |
| Maintenance | Bakım | |
| Refurbishment | Yenileme | Kapsamlı bakım/yeniden tasarım |
| Running Costs | İşletme Giderleri | Aylık sabit giderler |
| Breakdown | Arıza | |
| Inspection | Denetim | |
| Infrastructure | Altyapı | Jeneratör, pompa vb. |

#### Eğlence Birimi Durumları
| İngilizce | Türkçe | Not |
|-----------|--------|-----|
| Aging | Eskiyen | Prestij düşüş aşaması |
| Classic | Klasik | Bonus prestij aşaması |
| Established | Yerleşik | Normal işletim aşaması |
| Resurging | Canlanıyor | Prestij yükseliş aşaması |
| Reputation | İtibar | Ziyaretçi çekicilik skoru |
| Condition | Durum | Fiziksel yıpranma durumu |

#### Personel
| İngilizce | Türkçe | Not |
|-----------|--------|-----|
| Patrol Zone | Devriye Bölgesi | Personel görev alanı |
| Training | Eğitim | Personel seviye sistemi |
| Wage | Maaş | |
| Morale | Moral | Personel memnuniyet skoru |
| Ride Attendant | Biniş Görevlisi | Eğlence birimi operatörü |
| Workload | İş Yükü | |

#### Ziyaretçi İstatistikleri
| İngilizce | Türkçe | Not |
|-----------|--------|-----|
| Happiness | Mutluluk | Genel memnuniyet |
| Hunger | Açlık | |
| Thirst | Susuzluk | |
| Energy | Enerji | Yorgunluk karşıtı |
| Toilet Need | Tuvalet İhtiyacı | |
| Mood | Ruh Hali | Anlık durum |
| Thought | Düşünce | guest_thought kategorisi |
| Nausea Tolerance | Bulantı Toleransı | |
| Queue Tolerance | Sıra Bekleme Sabrı | |
| Fear Tolerance | Korku Toleransı | |
| Price Tolerance | Fiyat Toleransı | |

#### UI / Oyun Modları
| İngilizce | Türkçe | Not |
|-----------|--------|-----|
| Scenario | Senaryo | Belirli hedefleri olan oyun modu |
| Planet Points | Planet Points | Oyun adından gelir, çevrilmez |
| Tech Tree | Araştırma Ağacı | |
| Heatmap | Isı Haritası | Sorun görselleştirme |
| Season Track | Sezon Takibi | |
| Trigger Sequence | Olay Zinciri | Event tetikleme sistemi |
| Footprint | Zemin Alanı | Yapının kapladığı alan |
| Station | İstasyon | Biniş-iniş noktası |
| Track Element | Ray Elementi | Ray bağlantı parçası |

---

## 4. Stil Rehberi Güncellemeleri

### 4.1 Guest Thoughts ve Diyalog Tonu

Ziyaretçi düşünceleri ve diyaloglar yazılı Türkçe normlarına uyar. Samimi, birinci tekil, spontane hissettirmeli — ama ağız/sokak argosundan uzak.

**Kullanılabilir:**
- Doğal ünlemler: "Vay be!", "Müthiş!", "Harika!", "İnanılmaz!", "Berbat!"
- Duygu ifadeleri: "Sabırsızlanıyorum", "Dayanamıyorum", "Mükemmeldi"

**Kullanılmaz:**
- Ağız sözcükleri: "valla", "yahu", "be", "ya" (cümle sonu)
- Kaba argo: "pes artık", "yeter yahu"

**Örnekler:**
- ✅ "En sevdiğim eğlence birimine bineceğim, sabırsızlanıyorum!"
- ✅ "Bu kadar kuyruğa değmez, bir daha gelmem!"
- ❌ "Valla favorime bineceğim, dayanamıyorum yahu!"

### 4.2 Yapılmaması Gerekenler

| Hata | Yanlış | Doğru |
|------|--------|-------|
| Birebir çeviri | "up, up and away" → "yukarı, yukarı ve uzaklara" | "gökyüzüne fırlatır" |
| Yanlış terim | "ride" → "çekici" | "Eğlence Birimi" |
| Aşırı resmi | "deneyiminizi başlatın" | "hadi başlayalım" |
| Aşırı argo | "valla harika bir gün" | "Harika bir gün!" |
| İngilizce yapı | "Bu çekici {StartTime} içinde Klasik olacak" | "Bu eğlence birimi {StartTime} sonra Klasik aşamasına geçer" |

### 4.3 Bağlam Katmanları

| İçerik tipi | Ton | Örnek |
|-------------|-----|-------|
| UI buton/etiket | Kısa, net, emir kipi | "Kaydet", "Oyna" |
| Tooltip | 1-2 cümle, samimi, 2. tekil | "Bakım maliyetini gösterir" |
| Ride açıklaması | Akıcı, heyecan verici pazarlama dili | "Nefes kesen bir macera seni bekliyor!" |
| Guest thought | Doğal yazılı konuşma, birinci tekil | "Muhteşemdi, bir daha bineceğim!" |
| Tutorial | Öğretici, sıcak, adım adım | "Şimdi bir eğlence birimi yerleştir." |
| Kariyer diyalogu | Doğal, karaktere özgü | Karakterin kişiliğine uygun |

---

## 5. CLAUDE.md İçeriği

Projenin kök dizininde oluşturulacak. Her Claude Code oturumunda otomatik yüklenir.

```
# Planet Coaster 2 Türkçe Yama — Claude Kılavuzu

## Çeviri Seansına Başlamadan Önce ZORUNLU
1. glossary.json oku — tüm onaylı terimler burada
2. docs/STYLE_GUIDE.md oku — ton ve üslup kuralları
3. Hangi içerik tipini çevirdiğini belirle
4. O içerik tipinin ton kuralını uygula

## Asla Yapma
- "ride" veya "attraction" için "çekici" kullanma
- Cümle yapısını İngilizceden birebir çevirme
- "valla", "yahu", "be", "ya" (cümle sonu) kullanma
- Glossary'de olmayan terimler için kullanıcıya sormadan çeviri üretme

## Şüpheye Düştüğünde
- Yeni terim gerekiyorsa → önce kullanıcıya sor, glossary'e ekle, sonra çevir
- "Attraction" bağlama göre: UI/başlık → "Aktivite"; pazarlama → "Heyecan"
- Aynı metinde "Thrill" ve "Attraction" birlikte geçiyorsa "Aktivite" kullan

## Deploy Yöntemi
Mod klasörü crash yapıyor — kullanılmaz. Build sonrası şu dosyalar değiştirilmeli:
- Content0/Localised/English/UnitedStates/Loc.ovl
- Content0/Localised/English/UnitedKingdom/Loc.ovl
Orijinaller .bak uzantısıyla yedekli.
```

---

## 6. Validate.py Güncellemeleri

### 6.1 Yeni Kural: Yasaklı Terimler
```python
FORBIDDEN_TERMS = {
    "çekici": "Eğlence Birimi veya Aktivite",
    "misafir": "Ziyaretçi",
    "lunapark treni": "Hız Treni",
}
```
Eşleşme bulunursa: `[HATA] Yasaklı terim: "çekici" — kullan: "Eğlence Birimi veya Aktivite"`

### 6.2 Yeni Kural: Argo Uyarısı
```python
COLLOQUIAL_TERMS = [
    "valla", "yahu", "pes artık", "yeter yahu",
]
```
Eşleşme bulunursa: `[UYARI] Argo/ağız sözcüğü: "valla" — yalnızca onaylı bağlamlarda kullanılabilir`

### 6.3 Çıktı Formatı
```
[HATA]   infopanel_b4_translated → "çekici" yasaklı terim (33 string)
[UYARI]  guest_thought_b1_translated → "valla" argo sözcük (3 string)
[TAMAM]  ContentPDLC1/tr.json — 33 string, sorun yok
────────────────────────────────────────────────────────────
Toplam: 2 hata, 1 uyarı
```

---

## 7. Mevcut Çevirileri Düzeltme Planı

### Aşama 1 — Terminoloji Düzeltmeleri (Önce)
"çekici" ve diğer glossary ihlallerini toplu tespit et, bağlamına göre doğru terimle değiştir.

**Dosyalar ve tahmini "çekici" sayısı:**
- `infopanel_b4_translated.json`: 33
- `Content0/tr.json`: 74
- `tutorialscreen_b2_translated.json`: 8
- `infopanel_b5_translated.json`: 6
- `infopanel_b3_translated.json`: 4
- `parkmanagement_b2_translated.json`: 4
- `parkmanagement_b3_translated.json`: 4
- `sandboxsettings_translated.json`: 4
- `notification_translated.json`: 5
- `tutorialscreen_b1a_translated.json`: 3
- `infopanel_b1_translated.json`: 1
- `vo_translated_b2.json`: 1

### Aşama 2 — Kalite Düzeltmeleri (Öncelik Sırası)
Terminoloji değişikliği yeterli olmayan dosyalar, içerik tipine göre yeniden çevrilir:

| Öncelik | Dosya grubu | Sebep |
|---------|-------------|-------|
| 1 | infopanel (b1-b5) | En fazla hata, UI'ın kalbi |
| 2 | parkmanagement, notification | Sık görünen yönetim metinleri |
| 3 | tutorialscreen | Yeni oyuncuların ilk gördüğü |
| 4 | sandboxsettings | Mod açıklamaları |
| 5 | guest_thought (b1, b3) | Argo sorunu |
| 6 | Content0/tr.json (etkilenen kısım) | Ana dosya, büyük kapsam |

### Aşama 3 — Tasarım Dokümanı Düzeltmesi
`docs/superpowers/specs/2026-04-13-turkce-yama-design.md` içinde:
- Bölüm 7 (Dil Değiştirme Stratejisi): "Çekçe" → "English (US)" olarak güncellenir
- Mod yapısı: `Czech/CzechRepublic/Loc.ovl` → `English/UnitedStates/Loc.ovl` ve `English/UnitedKingdom/Loc.ovl`

---

## 8. Bellek Güncellemesi

`feedback_guest_thoughts_turkish.md` dosyası güncellenir:
- "yahu", "valla", "be" önerisi → "kullanma" olarak tersine çevrilir
- Yeni ton kuralı: doğal yazılı konuşma dili, ağız argosundan uzak

---

## 9. Çelişki Giderme Özeti

| Çelişki | Durum | Çözüm |
|---------|-------|-------|
| Memory "valla/yahu" öner ↔ kullanıcı "kullanma" | KRİTİK | Memory güncellenir |
| Tasarım dok "Czech" ↔ gerçek "English US/UK" | ORTA | Tasarım dok güncellenir |
| Glossary "Eğlence Birimi" ↔ çevirilerde "çekici" | KRİTİK | Tüm dosyalar düzeltilir |
| STYLE_GUIDE guest thoughts tonu eksik | ORTA | STYLE_GUIDE genişletilir |
| CLAUDE.md yok | KRİTİK | CLAUDE.md oluşturulur |
