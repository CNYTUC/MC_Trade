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
print(f"Zaman: {IstSaat}\n🚀 MC Test Başlatıldı!\n")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Donguyu Başlat
while True:

    # 1) INTERNET KONTROL
    internet_kontrol = True
    ust_donguye_gec = False  # Kontrol bayrağını en dışta tanımlıyoruz
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    if internet_kontrol:

        # RİSK ÇÖZÜLDÜ: Ay ve günü toplamak yerine yan yana birleştirip (örn: "0524" -> 524) benzersiz bir sayı yapıyoruz
        ilk_kontrol_tarih = int(f"{f_zaman.IstanbulAy()}{f_zaman.IstanbulGun()}")

        while True:
            # En hızlı servisler öncelikli kontrol ediliyor
            internet_var_mi = f_int.kontrolByGoogle() or f_int.kontrolByhttpbin()

            if internet_var_mi:
                Msj = "🌐 İnternet bağlantısı aktif, sistem hazır."
                print(f_str.MsjBasari(Msj))
                break  # İçteki internet döngüsünü kırar, dıştaki akışa geçer

            else:
                # Güncel tarihi yine birleşik sayı olarak alıyoruz
                Yeni_kontrol_tarih = int(f"{f_zaman.IstanbulAy()}{f_zaman.IstanbulGun()}")

                if ilk_kontrol_tarih == Yeni_kontrol_tarih:
                    Msj = "❌ Başarısız: Bağlantı hatası! Ertesi güne kadar, 10 sn ara ile tekrar denenecek!!!"
                    print(f_str.MsjIkaz(Msj))
                    f_zaman.Bekle(10)
                else:
                    # Gün kesinlikle değişti (Ay geçişleri dahil asla çakışmaz)
                    ust_donguye_gec = True
                    break  # İçteki internet döngüsünü kırar

    # >>> DOĞRU YER: İç döngü tamamen bittikten sonra ana while hizasında kontrol ediyoruz <<<
    if ust_donguye_gec:
        print("🔄 Gün değiştiği için sistem ana döngünün başına yönlendiriliyor...")
        continue  # Ana 'while True' döngüsünün en başına zıplar

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

        # Eğer saat 17:15'ten erken ise...
        if saat < 17 or (saat == 17 and dakika < 15):
            print(f"⏰ Saat henüz {saat:02d}:{dakika:02d}. İşlem için 17:15 bekleniyor...")

            # İşlemcinin yorulmaması için bekleme
            f_zaman.Bekle(10)

            continue  # Döngünün en başına döner
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------


    # 3) KULLANICI KONTROL
    kullanici_kontrol = True
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    while True:
        conf.tum_kullanicilar = sbase.get_all_users()
        i = 0
        for kullanici in conf.tum_kullanicilar:
            i = i + 1
        if i  > 0:
            Msj = f"{i} kullanıcı için işlem başlatılıyor."
            print(f_str.MsjBasari(Msj))
            break
        else:
            Msj: str = f"❌ Başarısız: Adına işlem yapılacak kullanıcı bulunamadı!!!"
            print(f_str.MsjHata(Msj))













    # -----------------------------------------------------------------------------
    # 2) BORSA İŞLEMLERİ (İnternet başarıyla bağlandıysa kod buraya ulaşır)
    # -----------------------------------------------------------------------------
    print("🚀 Başarılı! İnternet var ve zaman uygun. Borsa emirleri tetikleniyor...")

    # Not: Eğer borsa kodlarının da sonsuza kadar dönmesini istemiyorsanız,
    # iş bitiminde buraya ana döngüyü kıracak bir 'break' koyabilirsiniz.

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------




#
#

#
#
# # 3) Hisse Senedi Listesini Çek
#
# conf.tum_hisseler = sbase.get_all_bist()
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

