# Katkıda Bulunma Rehberi

## Nasıl Çevirmen Olurum?

1. Bu depoyu **fork** et
2. Kendi fork'unu **clone** et
3. `translations/<ContentPack>/tr.json` dosyasından çevirmek istediğin bir parça seç
4. `translation` alanlarını doldur, `status` alanını `translated` yap
5. Değişikliklerini **commit** et ve fork'una **push** et
6. **Pull request** aç

## Çeviri Kuralları

Çevirmeden önce mutlaka oku:
- [Stil Rehberi](STYLE_GUIDE.md)
- [glossary.json](../glossary.json) — Terimler sözlüğü

## Lokal Doğrulama

PR açmadan önce:
```bash
python tools/validate.py
```

İlerlemeni görmek için:
```bash
python tools/validate.py --stats
```

## PR Süreci

1. GitHub Actions otomatik `validate.py` çalıştırır
2. En az 1 maintainer çevirini inceler
3. Glossary ve stil rehberine uygunluk kontrol edilir
4. Onaylanan PR merge edilir

## Yeni Glossary Terimi Önerme

1. `glossary.json`'a terimi ekle (neden gerektiğini açıkla)
2. PR başlığı: `glossary: add <Term>`
3. PR açıklamasında terimin oyundaki bağlamını ve neden önerdiğin çeviriyi tercih ettiğini yaz

## Geliştirici Kurulumu

Bkz: [docs/DEVELOPMENT.md](DEVELOPMENT.md)

## İletişim

- GitHub Issues: Sorular, hata raporları
