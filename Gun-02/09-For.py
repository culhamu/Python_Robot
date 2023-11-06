isimler = ["Mustafa","Ali","Adem"]


for e in isimler:
    print(e)

isimler.sort()
print(isimler)    

for index ,eleman in enumerate(isimler):
    print(f"{index}:{eleman}")   

for i in range(0,10):
    print(i)   

for i in range(1, 11):
    print(i, end=" ")     

for i in range(10):
    for e in range(20):
        print(i,e)