
#sayi1 = input ("Lütfen bir sayi girin")
#sayi2 = input ("Lütfen bir sayi daha girin")

#print(int(sayi1)+int(sayi2))


while True:
    try:
        sayi1 = input("Lütfen bir sayi girin:")
        sayi2 = input("Lütfen bir sayi daha girin:")

        print(int(sayi1)+int(sayi2))
        break

    except:
            print("Lütfen bir sayi girin!")
      