isimler = ["Mustafa","Ahmet","Murat"]


def kontrol(isimler):
    return 'u' in isimler
    
print(list(map(kontrol,isimler) ))   

print(list(filter(kontrol,isimler)))


if "u" in "Hakan":
    print(True)
else:
    print(False)    