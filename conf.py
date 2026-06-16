import modules.supabaseFnks as sbase

# LOG KAYITLARI
# TARIH - SAAT - USER - OLAY
# log_kayitlari = None

# SUPABASEDEN ÇEKİLEN DEĞİŞKENLER
# ------------------------------------------------------------------
# *** AYARLAR
def IslemSaati(): return sbase.get_set_by_key("islem_SaatDakika")
def GtmIstFark(): return int(sbase.get_set_by_key("gtm_ist_fark"))
def KacGunlukVeri(): return sbase.get_set_by_key("kac_gunluk_veri")

# *** TATILLER
def tum_tatiller(): return sbase.get_all_holidays()

# *** KULLANICILAR
def tum_kullanicilar(): return sbase.get_all_users()

# *** HISSELER
def tum_hisseler(): return sbase.get_all_bist()



# TUTULAN DEĞİŞKENLER
# ------------------------------------------------------------------

# Verisi çekilebilen hisselerin fiyat tabloları
# ------------------------------------------------------------------
hisse_verileri = None

# Verisi çekilebilen hisse kodları
# ------------------------------------------------------------------
basarili_hisseler = None

# Verisi çekilemeyen hisse kodları
# ------------------------------------------------------------------
basarisiz_hisseler = None

# SADECE RAPORLAMA İÇİN KULLANILIYOR
# ------------------------------------------------------------------
# Her hissenin veri çekme durumunu tutar
# Örnek:
# [
#   {"Kod": "THYAO", "Durum": "✅"},
#   {"Kod": "ADLVY", "Durum": "❌"}
# ]
veri_durumlari = None

# ANALİZ İÇİN KULLANILAN DEĞİŞKENLER
# ------------------------------------------------------------------
analiz_sonuclari = None
elenenler = None
analiz_hatalari = None





