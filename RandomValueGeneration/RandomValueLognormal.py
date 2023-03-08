import random
import math

adet = int(input("Kaç adet rastsal değer üretilecek : "))
ortalama= float(input("Lognormal dağılım ortalaması : "))
std = float(input("Lognormal standart sapması : "))
pi = math.pi
e = math.e
for i in range(adet):
    rnd=random.random()
    a=(-1*(math.log(rnd)-ortalama)**2)/(2*std**2)
    r = (1/(std*rnd*(2*pi)**.5))*e**(a)
    print (i,". ",rnd, "---",r)

