from classes import *

mesaj = """HESAP MAKİNESİ
1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
5- Karakök
6- Kök al
7- Yüzde
8- Grand Total
9- Hesap Makinesini Sıfırla
10- Çıkış"""

print(mesaj)
hafiza = Hafiza()

def calculator():
    while True:
        print(f"Güncel hafıza: {hafiza.goster()}")
        islem = int(input("işlem seçin : "))
        try:
            if islem in [1, 2, 3, 4, 6, 7]:
                if not hafiza.goster() == 0:
                    s1 = hafiza.goster()
                else:
                    s1 = int(input("sayı1: "))
                s2 = int(input("sayı2: "))

                if islem == 1:
                    nesne = Toplama()
                elif islem == 2:
                    nesne = Cikarma()
                elif islem == 3:
                    nesne = Carpma()
                elif islem == 4:
                    nesne = Bolme()
                elif islem == 6:
                    nesne = KokAl()
                elif islem == 7:
                    nesne = Yuzde()

                total = nesne.hesapla(s1, s2)
                hafiza.ekle(total)
                print(f"Yeni sonuç: {total}")

            elif islem == 5:
                if hafiza.goster() != 0:
                    s = hafiza.goster()
                else:
                    s = int(input("sayı: "))

                nesne = Karakok()
                total = nesne.hesapla(s)
                hafiza.ekle(total)
                print(f"Yeni sonuç: {total}")

            elif islem == 8:
                print(f"Grand Total: {hafiza.goster()}")

            elif islem == 9:
                hafiza.temizle()
                print("Hafıza temizlendi.")

            elif islem == 10:
                print("çıkış yapılıyor...")
                break

            else:
                print("Hatalı seçim, tekrar deneyiniz.")

        except Exception as err:
            print("Hata:", err)

calculator()


