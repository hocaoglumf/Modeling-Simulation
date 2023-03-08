import random
import math
#print(math.sin(3.1415926535897932384626433832795/2))

def Sin(x):
    return math.sin(x)

def Cos(x):
    return math.cos(x)


n= int(input("Yineleme :"))
m = int(input("Oran :"))
tRnd=0
inFun=0
outFun=0
for i in range(0,n):
    rndx=random.random()*(math.pi /m)
    rndy=random.random()
    if (Sin(rndx)<=rndy):
        outFun +=1
    else:
        inFun+=1
print("Fonksiyon Altında Kalan: ",inFun, " Fonksiyonun üstünde Kalan : ", outFun)
print(3.14/m*inFun/(outFun+inFun))
