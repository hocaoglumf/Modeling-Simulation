import random

adet = int(input("Kaç adet rastsal değer üretilecek : "))
alt= float(input("Düzgün dağılım alt değeri : "))
ust= float(input("Düzgün dağılım üst değeri : "))

for i in range(adet):
    rnd = random.random()
    drs = alt + rnd *(ust-alt)
    aciklama=str(alt)+"+"+str(round(rnd,5))+"*("+str(ust)+"-"+str(alt)+")="
    print(i+1,". ", aciklama , round(drs,5))
