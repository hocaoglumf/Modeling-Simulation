import random
import math
adet = int(input("Kaç adet rastsal değer üretilecek : "))
ortalama= float(input("Üstel dağılım ortalaması : "))
randomlist=[]
for i in range(adet):
    rnd = random.random()
    aciklama="RV"+str(i+1)+".=" + str(-1)+"*"
    aciklama +=str(ortalama)+"*ln(1-" +str(round(rnd,5)) +")"
    rndv=round(-1*ortalama* math.log(1-rnd),5)
    randomlist.append(rndv)
    print (aciklama, "=", rndv)
print(randomlist)
print("[",min(randomlist),",",max(randomlist),"]" )