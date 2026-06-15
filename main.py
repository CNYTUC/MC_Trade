import conf

from fonksiyonlar import InternetIslem as f_int
from fonksiyonlar import StringIslem as f_str
from fonksiyonlar import ZamanIslem as f_zaman

import modules.veri as veri
import modules.analiz as analiz
import modules.supabaseFnks as sbase


# 0) Hoşgeldiniz
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
print(f"Zaman: {f_zaman.IstanbulSaatSaniye()}\n🚀 MC Trade Uygulamasına Hoşgeldiniz.\n")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Donguyu Başlat
while True:

    #DEĞİŞKENLER
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # Dongulerde gun atladı mı kontrol etmek için gerekli.
    dongu_tarihi = f_zaman.IstanbulGun()
    # Her turda sıfırlıyoruz
    ust_donguyu_basa_sar = False




    # 1) INTERNET KONTROL
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

    while True:
        # En hızlı servisler öncelikli kontrol ediliyor
        internet_var_mi = f_int.kontrolByGoogle() or f_int.kontrolByhttpbin()

        if internet_var_mi:

            Msj = "🌐 İnternet bağlantısı aktif, sistem hazır..."
            print(f_str.MsjBasari(Msj))

            break

        else:

            Msj = "❌ Bağlantı hatası! 15 sn ara ile tekrar denenecek!!!"
            print(f_str.MsjIkaz(Msj))
            f_zaman.Bekle(15)

        if f_zaman.gun_degisti_mi(dongu_tarihi):
            print(f_str.MsjIkaz("📅 Gün değişti. Ana kontroller yeniden başlatılıyor..."))
            ust_donguyu_basa_sar = True
            break  # İç döngüyü tamamen kırar ve dışarı fırlatır

    # İç döngü kırıldıktan sonra buraya gelir:
    if ust_donguyu_basa_sar:
        continue  # İşte bu komut

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------



    #2.1) HAFTA SONU KONTROLU
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

    while True:

        # bugün hafta sonu değil ise döngüden çık ve işlemlere başla
        if not f_zaman.HaftaSonuMu(f_zaman.IstanbulZaman()):  # hafta sonu değil ise

            # Bugün tatil değilse döngüden çık ve ana işlemleri başlat
            print(f"✅ Hafta Sonu değil.")
            break


        else:  # hafta sonu ise

            Msj = "❌ Hafta sonu olduğu için işlem yapılmayacak!!!\n15dk sonra tekrar denenecek..."
            print(f_str.MsjIkaz(Msj))

            f_zaman.Bekle(15 * 60)

        if f_zaman.gun_degisti_mi(dongu_tarihi):
            print(f_str.MsjIkaz("📅 Gün değişti. Ana kontroller yeniden başlatılıyor..."))
            ust_donguyu_basa_sar = True
            break  # İç döngüyü tamamen kırar ve dışarı fırlatır

    # İç döngü kırıldıktan sonra buraya gelir:
    if ust_donguyu_basa_sar:
        continue  # İşte bu komut

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------




    #2.2) TATIL GUNU KONTROLU
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

    # 'TUM TAILLERI CEK'
    conf.tum_tatiller = sbase.get_all_holidays()
    Tatiller = sorted([str(u["TARIH"]) for u in conf.tum_tatiller])

    # eğer tatil listesi boş değilse kontrol yap
    if len(Tatiller) > 0:

        while True:

            bugun_standart = f_zaman.IstanbulGun()  # ÖR 11/09/2024
            bugun_standart = f_zaman.tarih_format_değistir(bugun_standart)

            if not bugun_standart in Tatiller:
                # Bugün tatil değilse döngüden çık ve ana işlemleri başlat
                print(f"✅ Resmi tatil değil.")
                break

            if bugun_standart in Tatiller:
                Msj = f"❌ Bugün ({bugun_standart}) resmi tatil! İşlem yapılmayacak. Günün bitmesi bekleniyor...\n15dk sonra tekrar denenecek..."
                print(f_str.MsjIkaz(Msj))

                f_zaman.Bekle(15 * 60)

            if f_zaman.gun_degisti_mi(dongu_tarihi):
                print(f_str.MsjIkaz("📅 Gün değişti. Ana kontroller yeniden başlatılıyor..."))
                ust_donguyu_basa_sar = True
                break  # İç döngüyü tamamen kırar ve dışarı fırlatır

    # İç döngü kırıldıktan sonra buraya gelir:
    if ust_donguyu_basa_sar:
        continue  # İşte bu komut

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------




    # # 2.3) SAAT KONTROL
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    #
    # # İŞLEMİN BAŞLAYACAĞI SAATİ VE GMT IST FARKINI SUPABASE'DEN ÇEK
    # conf.gtm_ist_fark = int(sbase.get_set_by_key("gtm_ist_fark"))  # ÖR: 3
    # conf.islem_SaatDakika = f_zaman.saate_cevir(sbase.get_set_by_key("islem_SaatDakika"))
    #
    # islem_saat = conf.islem_SaatDakika #17:15
    # while True:
    #
    #     aktif_Saat = f_zaman.saate_cevir(f_zaman.IstanbulSaat())  # Örneğin 16:45
    #
    #     if aktif_Saat >= islem_saat:
    #
    #         Msj = "⏰ Saat geçerli, sistem hazır..."
    #         print(f_str.MsjBasari(Msj))
    #
    #         break
    #
    #     else:
    #
    #         saat_farki_dakika = f_zaman.saat_farki_hesapla(islem_saat, aktif_Saat)
    #
    #         # Olası bir hesaplama hatasına karşı koruma (Negatif değer kontrolü)
    #         if saat_farki_dakika <= 0:
    #             break
    #
    #         Msj = f"⏰ Saat henüz {aktif_Saat}. İşlem için {islem_saat} bekleniyor... (Kalan: {saat_farki_dakika} dk)\n5dk sonra tekrar denenecek..."
    #
    #         f_zaman.Bekle(5 * 60)
    #
    #     if f_zaman.gun_degisti_mi(dongu_tarihi):
    #         print(f_str.MsjIkaz("📅 Gün değişti. Ana kontroller yeniden başlatılıyor..."))
    #         ust_donguyu_basa_sar = True
    #         break  # İç döngüyü tamamen kırar ve dışarı fırlatır
    #
    # # İç döngü kırıldıktan sonra buraya gelir:
    # if ust_donguyu_basa_sar:
    #     continue  # İşte bu komut
    #
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------




    # 3) KULLANICI KONTROL
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

    while True:

        conf.tum_kullanicilar = sbase.get_all_users()
        Kullanici_Sayisi = len(conf.tum_kullanicilar)

        # 2. Aktif kullanıcıları tek satırda filtreleyip sayısını alıyoruz
        # Supabase'den boolean geldiği için direkt 'if u.get("is_active")' yeterlidir
        AktifKullanici_Sayisi = len([u for u in conf.tum_kullanicilar if u.get("is_active")])

        if Kullanici_Sayisi > 0 and AktifKullanici_Sayisi > 0:

            Msj = f"✅ {AktifKullanici_Sayisi} Aktif kullanıcı bulundu. İşlem başlatılıyor..."
            print(f_str.MsjBasari(Msj))
            break  # Başarılı ise döngüden çık

        # 3. Koşul kontrolü (Daha okunabilir hali)
        if Kullanici_Sayisi == 0 or AktifKullanici_Sayisi == 0:

            Msj: str = "❌ Başarısız: Adına işlem yapılacak Aktif kullanıcı bulunamadı!!!\n15dk sonra tekrar denenecek..."
            print(f_str.MsjHata(Msj))
            f_zaman.Bekle(15*60)

        if f_zaman.gun_degisti_mi(dongu_tarihi):

            print(f_str.MsjIkaz("📅 Gün değişti. Ana kontroller yeniden başlatılıyor..."))
            ust_donguyu_basa_sar = True
            break  # İç döngüyü tamamen kırar ve dışarı fırlatır

    # İç döngü kırıldıktan sonra buraya gelir:
    if ust_donguyu_basa_sar:
        continue  # İşte bu komut
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------




    # 4) HİSSE SENEDİ LİSTESİ ÇEK
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

    while True:

        conf.tum_hisseler = sbase.get_all_bist()
        HisseSenediListeSayisi = len(conf.tum_hisseler)

        if HisseSenediListeSayisi > 0:

            Msj = f"✅ {HisseSenediListeSayisi} Hisse senedi değerlendirilecek."
            print(f_str.MsjBasari(Msj))
            break  # Başarılı ise döngüden çık

        else:

            Msj: str = "❌ Başarısız: Adına işlem yapılacak Hisse Senedi bulunamadı!!!\n5dk sonra tekrar denenecek..."
            print(f_str.MsjHata(Msj))

            f_zaman.Bekle(5 * 60)

        if f_zaman.gun_degisti_mi(dongu_tarihi):
            print(f_str.MsjIkaz("📅 Gün değişti. Ana kontroller yeniden başlatılıyor..."))
            ust_donguyu_basa_sar = True
            break  # İç döngüyü tamamen kırar ve dışarı fırlatır

    # İç döngü kırıldıktan sonra buraya gelir:
    if ust_donguyu_basa_sar:
        continue  # İşte bu komut

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------


    #ANA İŞLEMLERİ BAŞLAT

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

    # 5) HİSSE SENEDİ VERİLERİNİ ÇEK
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

    Msj = "Veriler Alınıyor... \n -------------------"
    print(f_str.MsjBasari(Msj))




    #Supabase'den çektiğiniz conf.tum_hisseler listesini fonksiyona gönderiyoruz
    conf.hisse_verileri, conf.veri_durumlari, conf.basarili_hisseler, conf.basarisiz_hisseler = veri.tum_hisselerin_verisini_cek(conf.tum_hisseler, gun=300)

    # Başarı durumlarını ekrana yazdırıyoruz
    veri.veri_durumlarini_yazdir(conf.veri_durumlari)
    print(f_str.MsjBasari(f"{len(conf.basarili_hisseler)} hissenin verisi çekildi."))
    print(f_str.MsjIkaz(f"{len(conf.basarisiz_hisseler)} hissede veri alınamadı."))

    # ANALIZE BAŞLA

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    analiz.analiz_sonuclarini_yazdir(conf.analiz_sonuclari)

    print("\nELENENLER")
    print("-" * 30)
    for sebep, adet in conf.elenenler.items():
        print(f"{sebep:20}: {adet}")

    if len(conf.analiz_hatalari) > 0:
        print("\nANALİZ HATALARI")
        print("-" * 30)
        for hata in conf.analiz_hatalari:
            print(hata)







