import random
import math

adet = int(input("Kaç adet rastsal değer üretilecek : "))
alfa= float(input("Alfa parametresi: "))
beta= float(input("beta parametresi: "))

for i in range(adet):
    rn =random.random()
    y = (-1/alfa * math.log(1-rn))**(1/beta)
    aciklama="RV"+str(i+1)+"=" + str(-1) +"/" + str(alfa) +"* ln(1-"+str(round(rn,5))+")**(1/"+str(beta)+")"
    print(aciklama,"=", round(y,5))