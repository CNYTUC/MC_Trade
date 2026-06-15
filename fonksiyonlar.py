# KUTUPHANELER
import requests                                              # INTERNET ICIN GEREKLI

class InternetIslem:

    @staticmethod
    # Yardımcı Fonksiyonlar
    def kontrolByhttpbin() -> bool:
        try:
            response = requests.get("https://httpbin.org", timeout=5)
            return response.status_code == 200
        except requests.RequestException as e:
            # Hatanın ne olduğunu konsolda görün
            # print(f"Hata oluştu: {e}")
            return False

    @staticmethod
    def kontrolByGoogle() -> bool:
        try:
            # allow_redirects=True ile yönlendirmeleri sonuna kadar takip etmesini söylüyoruz
            response = requests.head("https://google.com", timeout=5, allow_redirects=True)
            return response.status_code == 200
        except requests.RequestException:
            return False

# ─────────────────────────────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────────────────────────

class StringIslem:


    RESET = "\033[0m"

    class Kod:
        Bold = "\033[1m"
        Dim = "\033[2m"
        Underlined = "\033[4m"
        Blink = "\033[5m"
        Reverse = "\033[7m"
        Hidden = "\033[8m"

        Default = "\033[39m"
        Black = "\033[30m"
        Red = "\033[31m"
        Green = "\033[32m"
        Yellow = "\033[33m"
        Blue = "\033[34m"
        Magenta = "\033[35m"
        Cyan = "\033[36m"
        LightGray = "\033[37m"
        DarkGray = "\033[90m"
        LightRed = "\033[91m"
        LightGreen = "\033[92m"
        LightYellow = "\033[93m"
        LightBlue = "\033[94m"
        LightMagenta = "\033[95m"
        LightCyan = "\033[96m"
        White = "\033[97m"

        BackgroundDefault = "\033[49m"
        BackgroundBlack = "\033[40m"
        BackgroundRed = "\033[41m"
        BackgroundGreen = "\033[42m"
        BackgroundYellow = "\033[43m"
        BackgroundBlue = "\033[44m"
        BackgroundMagenta = "\033[45m"
        BackgroundCyan = "\033[46m"
        BackgroundLightGray = "\033[47m"
        BackgroundDarkGray = "\033[100m"
        BackgroundLightRed = "\033[101m"
        BackgroundLightGreen = "\033[102m"
        BackgroundLightYellow = "\033[103m"
        BackgroundLightBlue = "\033[104m"
        BackgroundLightMagenta = "\033[105m"
        BackgroundLightCyan = "\033[106m"
        BackgroundWhite = "\033[107m"

    @staticmethod
    def uygula(metin: str, *kodlar: str) -> str:
        return "".join(kodlar) + str(metin) + StringIslem.RESET

    @staticmethod
    def MsjHata(metin: str) -> str:
        return StringIslem.uygula(metin, StringIslem.Kod.Red, StringIslem.Kod.Bold)

    @staticmethod
    def MsjBasari(metin: str) -> str:
        return StringIslem.uygula(metin, StringIslem.Kod.Green, StringIslem.Kod.Bold)

    @staticmethod
    def MsjIkaz(metin: str) -> str:
        return StringIslem.uygula(metin, StringIslem.Kod.Yellow, StringIslem.Kod.Bold, StringIslem.Kod.BackgroundBlack)

# ─────────────────────────────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────────────────────────

# KUTUPHANELER
import time                                                  # Zaman
from datetime import datetime, timezone, timedelta, date     # Zaman

class ZamanIslem:

    # -------------------------------------------------------------------------

    @staticmethod
    def SistemGun():
        today = date.today()
        return today.strftime("%d/%m/%Y")

    @staticmethod
    def SistemSaat():
        now = datetime.now()
        return now.strftime("%H:%M")

    @staticmethod
    def SistemSaatSaniye():
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    @staticmethod
    def SistemZaman():
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    # -------------------------------------------------------------------------

    @staticmethod
    def GmtGun():
        now = datetime.now(timezone.utc)
        return now.strftime("%d/%m/%Y")

    @staticmethod
    def GmtSaat():
        now = datetime.now(timezone.utc)
        return now.strftime("%H:%M")

    @staticmethod
    def GmtSaatSaniye():
        now = datetime.now(timezone.utc)
        return now.strftime("%H:%M:%S")

    @staticmethod
    def GmtZaman():
        now = datetime.now(timezone.utc)
        return now.strftime("%d/%m/%Y %H:%M:%S")

    # -------------------------------------------------------------------------

    @staticmethod
    def IstanbulGun():
        now = datetime.now(timezone.utc) + timedelta(hours=3)
        return now.strftime("%d/%m/%Y")

    @staticmethod
    def IstanbulSaat():
        now = datetime.now(timezone.utc) + timedelta(hours=3)
        return now.strftime("%H:%M")

    @staticmethod
    def IstanbulSaatSaniye():
        now = datetime.now(timezone.utc) + timedelta(hours=3)
        return now.strftime("%H:%M:%S")

    @staticmethod
    def IstanbulZaman():
        now = datetime.now(timezone.utc) + timedelta(hours=3)
        return now.strftime("%d/%m/%Y %H:%M:%S")

    # -------------------------------------------------------------------------

    @staticmethod
    def HaftaSonuMu(Zaman_str: str):
        # 1. Gelen metni (string) datetime nesnesine dönüştürüyoruz
        zaman_nesnesi = datetime.strptime(Zaman_str, "%d/%m/%Y %H:%M:%S")

        # 2. Artık weekday() fonksiyonunu güvenle kullanabiliriz
        return zaman_nesnesi.weekday() in [5, 6]

    @staticmethod
    def gun_degisti_mi(baslangic_tarihi):
        now = datetime.now(timezone.utc) + timedelta(hours=3)
        aktif_tarih = now.strftime("%d/%m/%Y")

        return aktif_tarih != baslangic_tarihi

    @staticmethod
    def Bekle(Sure: int):
        time.sleep(Sure)

    @staticmethod
    def saat_farki_hesapla(saat1_str, saat2_str):
        # Saat formatını (Saat:Dakika) tanımlıyoruz
        saat_formati = "%H:%M"

        # Metinleri zaman nesnesine dönüştürüyoruz
        t1 = datetime.strptime(saat1_str, saat_formati)
        t2 = datetime.strptime(saat2_str, saat_formati)

        # Büyük saatten küçük saati çıkarıp farkı buluyoruz
        fark = t1 - t2

        # Farkı toplam dakika cinsinden alıyoruz
        toplam_dakika = int(fark.total_seconds() / 60)

        return toplam_dakika

    # Metinleri gerçek saat nesnesine çeviren fonksiyon
    @staticmethod
    def saate_cevir(saat_str):
        return datetime.strptime(saat_str, "%H:%M").time()

    # Metinleri gerçek tarih nesnesine çeviren fonksiyon
    @staticmethod
    def tarihe_cevir(saat_str):
        return datetime.strptime(saat_str, "%d/%m/%Y").time()

    # Tarih formatını değiştir.
    @staticmethod
    def tarih_format_değistir(tarih_str):
        return datetime.strptime(tarih_str, "%d/%m/%Y").strftime("%Y-%m-%d")