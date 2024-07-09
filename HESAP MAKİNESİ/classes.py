import math
class Toplama:
    def hesapla(self,sayi1,sayi2):
      return sayi1+sayi2

class Cikarma:
    def hesapla(self,sayi1,sayi2):
        if sayi1>sayi2:
            total = sayi1-sayi2
        else:
            total = sayi2-sayi1
        return total

class Carpma:
    def hesapla(self,sayi1,sayi2):
      return sayi1*sayi2

class Bolme:
    try:
        def hesapla(self,sayi1,sayi2):
            return sayi1/sayi2

    except Exception as err:
        print("hata: ", err)

class Karakok:
    def hesapla(self,sayi):
        if sayi<0:
            raise Exception("negatif bir sayının karakökü alınamaz.")
        elif sayi==0:
            raise Exception("sıfırın karakökü alınamaz.")
        else:
            return math.sqrt(sayi)

class KokAl:
    def hesapla(self,sayi1,sayi2):
        if sayi1<0 :
            raise Exception("negatif bir sayının karakökü alınamaz.")
        else:
            return sayi1**(1/sayi2)

class Yuzde:
    def hesapla(self, sayi1,sayi2):
       return (sayi1*sayi2)/100

class Hafiza:

  def __init__(self):
      self.hafiza = 0

  def ekle(self,deger):
      self.hafiza = deger

  def goster(self):
      return self.hafiza

  def temizle(self):
      self.hafiza = 0
