import requests
from bs4 import BeautifulSoup
url= "https://www.hdfilmcehennemi.nl/dizi/yuksek-satodaki-adam-izle-3/"

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    comments = soup.find_all("p",class_="comment-item-content")
    if not comments:
        print("yorum bulunamadı. dogru html sınıf adressını aldıgından emın ol")
    for comment in comments:
        print("*",comment.text.strip())
except requests.exceptions.RequestException as e:
    print(f"HTTP hatası: {e}")
except Exception as e:
    print(f"Hata: {e}")