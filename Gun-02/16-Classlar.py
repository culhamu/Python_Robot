class Insan():
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

    def bilgileriYaz(self):
        print(f"Kaullanicinin adi soyadi: {self.isim} {self.soyisim}. Yasi{self.yas}")  


    def __str__(self) -> str:
        print(f"{self.isim} {self.soyisim} {self.yas}")  

    def  __len__(self):
        return self.yas

Insan = Insan("Mustafa","Ademoglu",35)

Insan.bilgileriYaz()

print(str(Insan))
print(len(Insan))



class Mustafa(Insan):
    def __init__(self, isim, soyisim, yas):
        super().__init__(isim, soyisim, yas)