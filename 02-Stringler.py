metin = "Merhaba Dünya"

newMetin = metin.split()
print(newMetin)

#metin[baslangic:bitis:örüntüsü]
print(metin[0])
print(metin[0:10:2])#substring gibi
print(metin[:3])
print(metin[4:])
print(metin[::2])

print(metin.lower)
print(metin.replace("M","Y"))

print(len(metin))#len methodu uzunluğu verir

sonEleman = len(metin)-1
print(sonEleman)
print(metin[-1])
