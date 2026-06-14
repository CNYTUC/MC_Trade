import time  # Zaman
import conf
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

def IstanbulZamanSTR():
    gmt_zamani = datetime.now(timezone.utc)
    istanbul_farki = timedelta(hours=conf.spbase.gtm_ist_fark)
    istanbul_zamani = gmt_zamani + istanbul_farki
    return istanbul_zamani.strftime("%Y-%m-%d %H:%M:%S")

def IstanbulZaman():
    gmt_zamani = datetime.now(timezone.utc)
    istanbul_farki = timedelta(hours=3)
    istanbul_zamani = gmt_zamani + istanbul_farki
    return istanbul_zamani

def IstanbulYil(): return IstanbulZaman().year
def IstanbulAy(): return IstanbulZaman().month
def IstanbulGun(): return IstanbulZaman().day
def IstanbulSaat(): return IstanbulZaman().hour
def IstanbulDakika(): return IstanbulZaman().minute
def IstanbulSaniye(): return IstanbulZaman().second


def TimeStamp_GunFormat(timeStamp): return datetime.fromtimestamp(int(timeStamp) / 1000)