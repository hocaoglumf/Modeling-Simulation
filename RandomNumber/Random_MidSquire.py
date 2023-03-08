
number=int(input("Kac adet rastsal sayı üretilecek "))
while True:
    sayi=int(input("Bir Sayı Girini"))
    sayiS= str(sayi)
    if (len(sayiS)>=4):
        break
    else:
        print("Bu olmaz daha büyük")
n=0
rastsalSayilar=[]
while (number>n):
    oldSayi = sayi
    sayi=sayi**2
    sayiS= str(sayi)
    if (len(sayiS)%2==1):
        sayS="0"+sayiS
    x = (len(sayiS)-4)/2
    print(oldSayi, "  ",sayiS," ---> ", sayiS[int(x):4+int(x)])
    sayi= int(sayiS[int(x):4+int(x)])
    rastsalSayilar.append(sayi/10000)
    n+=1

print("Rastsal Sayılar: ", rastsalSayilar)