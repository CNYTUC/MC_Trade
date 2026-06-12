import requests


# Yardımcı Fonksiyonlar
def kontrolByhttpbin() -> bool:
    try:
        response = requests.get("https://httpbin.org", timeout=5)
        return response.status_code == 200
    except requests.RequestException as e:
        # Hatanın ne olduğunu konsolda görün
        # print(f"Hata oluştu: {e}")
        return False

def kontrolByGoogle() -> bool:
    try:
        # allow_redirects=True ile yönlendirmeleri sonuna kadar takip etmesini söylüyoruz
        response = requests.head("https://google.com", timeout=5, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False
