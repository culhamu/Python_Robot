def ekranaYaz():
    print("Merhaba")

ekranaYaz()  

def ekrann(cumle):
    print("Merhaba "+cumle)

ekrann("Mustafa")    


def karesiniAl(sayi : int)->int:
    return sayi **2

print(karesiniAl(123))

def defaultParametreAlanFonksiyon(isim = "Mustafa"):
    print(isim)

defaultParametreAlanFonksiyon("Mehmet")
defaultParametreAlanFonksiyon()

def sayilariTopla(sayi1,sayi2):
    print(sayi1+sayi2)

sayilariTopla(10,40)    

def birden_cok_sayi_topla(*sayilar)->int:
    toplam=0
    for i in sayilar:
        toplam+=i

        print(toplam)

birden_cok_sayi_topla(10.6,20,30.2,5)        
