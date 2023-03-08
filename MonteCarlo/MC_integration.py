import random
import math
n= int(input("Tekrar Sayısı :"))
#m = int(input("Oran :"))
m=1
tRnd=0
inFun=0
outFun=0
for i in range(0,n):
    rndx=random.random()*(math.pi/m)
    rndy=random.random()
    if (math.sin(rndx)<=rndy):
        outFun +=1
    else:
        inFun+=1
print("Fonksiyon Altındaki Alan: ",inFun, " Fonksiyon Dışı Alan: ", outFun)
print(math.pi/m*inFun/(outFun+inFun))