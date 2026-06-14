from pycparser.c_ast import While

import conf
import modules.supabaseFnks as sbase
import fonksiyonlar.f_str as f_str
import fonksiyonlar.f_internet as f_int
import fonksiyonlar.f_zaman as f_zaman
from modules.veri import tum_hisselerin_verisini_cek
from modules.veri import veri_durumlarini_yazdir

# 0) Hoşgeldiniz
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
IstSaat = f_zaman.IstanbulZamanSTR()
print(f"Zaman: {IstSaat}\n🚀 MC Trade Uygulamasına Hoşgeldiniz.\n")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Donguyu Başlat
while True:


    # 1) INTERNET KONTROL
    internet_kontrol = True
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    if internet_kontrol:

        while True:
            # En hızlı servisler öncelikli kontrol ediliyor
            internet_var_mi = f_int.kontrolByGoogle() or f_int.kontrolByhttpbin()

            if internet_var_mi:

                Msj = "🌐 İnternet bağlantısı aktif, sistem hazır."
                print(f_str.MsjBasari(Msj))

                break

            else:

                Msj = "❌ Başarısız: Bağlantı hatası! 10 sn ara ile tekrar denenecek!!!"
                print(f_str.MsjIkaz(Msj))
                f_zaman.Bekle(10)

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------



    # 2) ZAMAN KONTROL
    zaman_kontrol = False
    # *** BU VERI CANLIYA ALINDIĞINDA True olarak değiştirilmeli
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    if zaman_kontrol:

        saat = int(f_zaman.IstanbulSaat())
        dakika = int(f_zaman.IstanbulDakika())

        while True:

            # Eğer saat 17:15'ten erken ise...
            if saat < 17 or (saat == 17 and dakika < 15):
                print(f"⏰ Saat henüz {saat:02d}:{dakika:02d}. İşlem için 17:15 bekleniyor...")

                # İşlemcinin yorulmaması için bekleme
                f_zaman.Bekle(10)

            else:

                break

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------



    # 3) KULLANICI KONTROL
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

    while True:
        conf.tum_kullanicilar = sbase.get_all_users()

        # 1. Toplam kullanıcı sayısını len() ile direkt alıyoruz
        Kullanici_Sayisi = len(conf.tum_kullanicilar)

        # 2. Aktif kullanıcıları tek satırda filtreleyip sayısını alıyoruz
        # Supabase'den boolean geldiği için direkt 'if u.get("is_active")' yeterlidir
        AktifKullanici_Sayisi = len([u for u in conf.tum_kullanicilar if u.get("is_active")])

        # 3. Koşul kontrolü (Daha okunabilir hali)
        if Kullanici_Sayisi == 0 or AktifKullanici_Sayisi == 0:
            Msj: str = "❌ Başarısız: Adına işlem yapılacak Aktif kullanıcı bulunamadı!!!"
            print(f_str.MsjHata(Msj))

            # SİSTEMİ KORUMAK İÇİN KRİTİK DOKUNUŞ:
            # Kullanıcı bulunamadıysa tekrar sorgulamadan önce 10 saniye bekle
            print("10 saniye sonra tekrar denenecek...")
            f_zaman.Bekle(10)
        else:
            Msj = f"✅ {AktifKullanici_Sayisi} Aktif kullanıcı için işlem başlatılıyor."
            print(f_str.MsjBasari(Msj))
            break  # Başarılı ise döngüden çık

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

        if not HisseSenediListeSayisi == 0:

            Msj = f"✅ {HisseSenediListeSayisi} Hisse senedi değerlendirilecek."
            print(f_str.MsjBasari(Msj))
            break  # Başarılı ise döngüden çık

        else:

            Msj: str = "❌ Başarısız: Adına işlem yapılacak Hisse Senedi bulunamadı!!!"
            print(f_str.MsjHata(Msj))

            # SİSTEMİ KORUMAK İÇİN KRİTİK DOKUNUŞ:
            # Kullanıcı bulunamadıysa tekrar sorgulamadan önce 10 saniye bekle
            print("5dk sonra tekrar denenecek...")
            f_zaman.Bekle(300)

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------

        # 5) HİSSE SENEDİ VERİLERİNİ ÇEK
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------------------------
        # -----------------------------------------------------------------------------

        Msj = "Veriler Alınıyor... \n -------------------"
        print(f_str.MsjBasari(Msj))


        (
            conf.hisse_verileri,
            conf.veri_durumlari,
            conf.basarili_hisseler,
            conf.veri_hatalari
        ) = tum_hisselerin_verisini_cek(
            conf.tum_hisseler,
            gun=300
        )
    #
    #     veri_durumlarini_yazdir(conf.veri_durumlari)
    #
    #     print()
    #     print(f_str.MsjBasari(
    #         f"{len(conf.basarili_hisseler)} hissenin verisi çekildi."
    #     ))
    #
    #     print(f_str.MsjIkaz(
    #         f"{len(conf.basarisiz_hisseler)} hissede veri alınamadı."
    #     ))
    #
    #
    #
    #









# # 4) Hisse Senedi verilerini
#
# i = 0
#
# for x in conf.tum_hisseler:
#     i += 1
#
# if i == 0:
#     Msj = "❌ Başarısız: İşlem yapılacak hisse bulunamadı!!!"
#     print(f_str.MsjHata(Msj))
#
# else:
#     Msj = f"{i} Hisse Senedi bulundu."
#     print(f_str.MsjBasari(Msj))
#
#     (
#         conf.hisse_verileri,
#         conf.veri_durumlari,
#         conf.basarili_hisseler,
#         conf.veri_hatalari
#     ) = tum_hisselerin_verisini_cek(
#         conf.tum_hisseler,
#         gun=300
#     )
#
#     veri_durumlarini_yazdir(conf.veri_durumlari)
#
#     print()
#     print(f_str.MsjBasari(
#         f"{len(conf.basarili_hisseler)} hissenin verisi çekildi."
#     ))
#
#     print(f_str.MsjIkaz(
#         f"{len(conf.basarisiz_hisseler)} hissede veri alınamadı."
#     ))
#
#
#
#

