# Gerekli kütüphaneleri içe aktarıyoruz
import requests
from bs4 import BeautifulSoup

# Yorumları çekmek istediğimiz dizinin URL'si
url = "https://www.hdfilmcehennemi.nl/dizi/yuksek-satodaki-adam-izle-3/"

try:
    # Belirtilen URL'ye HTTP GET isteği gönderiyoruz
    response = requests.get(url)
    
    # İstek başarılı mı kontrol ediyoruz, değilse hata fırlatır
    response.raise_for_status()

    # Sayfa içeriğini BeautifulSoup ile parse ediyoruz
    soup = BeautifulSoup(response.content, "html.parser")

    # HTML içinden yorumların bulunduğu <p> etiketlerini, sınıf adıyla birlikte seçiyoruz
    comments = soup.find_all("p", class_="comment-item-content")

    # Eğer hiç yorum bulunamazsa kullanıcıyı bilgilendiriyoruz
    if not comments:
        print("Yorum bulunamadı. Doğru HTML sınıf adresini aldığınızdan emin olun.")

    # Her bir yorumu ekrana yazdırıyoruz
    for comment in comments:
        print("*", comment.text.strip())

# HTTP kaynaklı bir hata olursa yakalıyoruz
except requests.exceptions.RequestException as e:
    print(f"HTTP hatası: {e}")

# Diğer tüm hatalar burada yakalanır
except Exception as e:
    print(f"Hata: {e}")
