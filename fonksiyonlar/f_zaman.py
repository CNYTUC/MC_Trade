import time  # Zaman
from datetime import datetime, timezone, timedelta
from datetime import date

def Bekle(Sure: int):
    time.sleep(Sure)

def Saat():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def Gun():
    today = date.today()
    return today.strftime("%d/%m/%Y")

def GunSaat():
    return Gun() + " " + Saat()

def Gmt():
    return datetime.now(timezone.utc)

def IstanbulSaat():
    gmt_zamani = datetime.now(timezone.utc)
    istanbul_farki = timedelta(hours=3)
    return gmt_zamani + istanbul_farki

def TimeStamp_GunFormat(timeStamp): return datetime.fromtimestamp(int(timeStamp) / 1000)