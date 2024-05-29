class HesapMakinesi:
    def __init__(self, a, b):
        self.deger1 = a
        self.deger2 = b

    def toplama(self):
        return self.deger1 + self.deger2

    def cikarma(self):
        return self.deger1 - self.deger2

    def carpma(self):
        return self.deger1 * self.deger2

    def bolme(self):
        if self.deger2 == 0:
            return "Hata: Sifira bolme"
        return self.deger1 / self.deger2

    def mod(self):
        return self.deger1 % self.deger2

    def us_alma(self):
        return self.deger1 ** self.deger2

def kullanici_secimi():
    print("\nToplama (1), Cikarma (2), Carpma (3), Bolme (4), Mod (5), Us Alma (6)")
    secim = input("Lutfen yapmak istediginiz islemi secin (1-6): ")
    return secim

def degerleri_al():
    try:
        deger1 = float(input("Birinci Deger: "))
        deger2 = float(input("Ikinci Deger: "))
        return deger1, deger2
    except ValueError:
        print("Gecersiz giris. Lutfen sayisal degerler girin.")
        return None, None

def hesapla_ve_yazdir(secim, hesap):
    if secim == "1":
        print("\nToplama Sonucu: {}".format(hesap.toplama()))
    elif secim == "2":
        print("\nCikarma Sonucu: {}".format(hesap.cikarma()))
    elif secim == "3":
        print("\nCarpma Sonucu: {}".format(hesap.carpma()))
    elif secim == "4":
        print("\nBolme Sonucu: {}".format(hesap.bolme()))
    elif secim == "5":
        print("\nMod Sonucu: {}".format(hesap.mod()))
    elif secim == "6":
        print("\nUs Alma Sonucu: {}".format(hesap.us_alma()))
    else:
        print("Gecersiz secim. Lutfen tekrar deneyin.")

def main():
    while True:
        secim = kullanici_secimi()
        if secim not in ["1", "2", "3", "4", "5", "6"]:
            print("Gecersiz secim. Lutfen tekrar deneyin.")
            continue

        deger1, deger2 = degerleri_al()
        if deger1 is None or deger2 is None:
            continue

        hesap = HesapMakinesi(deger1, deger2)
        hesapla_ve_yazdir(secim, hesap)

        tekrar = input("\nBaska bir islem yapmak ister misiniz? (E/H): ")
        if tekrar.lower() != 'e':
            print("Programdan cikiliyor. Iyi gunler!")
            break

if __name__ == "__main__":
    main()
