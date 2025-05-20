# 🔍 Web Scraping Projesi: HTML'den Veri Çekme

Bu Python projesi, herhangi bir web sitesinden belirli HTML öğelerini çekmek amacıyla oluşturulmuştur.  
Örnek olarak bir sitedeki kullanıcı yorumları çekilmektedir ancak kod yapısı **herhangi bir veri türü** için uyarlanabilir.

---

## 🎯 Projenin Amacı

- Web sayfalarından **belirli HTML öğelerini** (örneğin yorumlar, başlıklar, fiyatlar) çekmeyi öğrenmek.
- `requests` ve `BeautifulSoup` kütüphanelerini kullanarak HTML içeriğini ayrıştırmak.
- Web scraping projeleri için temel bir şablon oluşturmak.

---

## 🧰 Gereksinimler

### 📦 Kullanılan Kütüphaneler

- `requests`: Web sayfasına HTTP isteği göndermek için.
- `beautifulsoup4`: HTML yapısını ayrıştırmak için.

### 🔧 Kurulum Komutu

```bash
pip install requests beautifulsoup4
```

## 🧠 Açıklamalar

| Kod | Açıklama |
|------|----------|
| `requests.get(url)` | Web sayfasını indirir |
| `raise_for_status()` | HTTP hatası varsa yakalar |
| `BeautifulSoup(...)` | HTML içeriği ayrıştırır |
| `find_all(...)` | Belirtilen etikete ve sınıfa sahip öğeleri seçer |
| `comment.text.strip()` | HTML etiketinden sadece metin kısmını temiz biçimde çeker |

---

## ⚠️ Uyarılar

- Kullandığınız sitenin kullanım koşullarına ve robots.txt politikasına uymalısınız.
- Eğer `find_all` sonuç döndürmüyorsa, sayfa yapısı değişmiş olabilir. Doğru HTML etiket ve sınıfını kullanmaya dikkat edin.
- Bazı siteler tarayıcı dışında gelen isteklere izin vermez. Gerekirse `headers` veya `User-Agent` eklemeniz gerekebilir.

---

## 📌 Not

Bu proje dizi/film sitelerine özgü değildir. Yalnızca scraping örneği olarak ilgili bir sayfa kullanılmıştır. Aynı yapı, haber siteleri, fiyat karşılaştırma sayfaları, e-ticaret ürünleri ve daha birçok alana kolayca uyarlanabilir.
