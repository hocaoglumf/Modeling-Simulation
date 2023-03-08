import random
import math
import matplotlib.pyplot as plt
from RandomValueGeneration import NormalRandomNumber


#adet = int(input("Kaç adet rastsal değer üretilecek : "))
#ortalama= float(input("Normal dağılım ortalaması : "))
#std = float(input("Normal standart sapması : "))

#nrsAdet= int(input("Normal rastsal sayı için kullanılacak rastsal sayı adedi : "))

def Normal(adet, ortalama, std):
    normal={}
    for i in range(adet):
        Nr= NormalRandomNumber.NormalRandomNumber(12)
        #Nr=Nr*(100)
        normal[Nr]= ortalama+std*Nr
    return normal


def Lognormal(adet, ortalama, std):
    pi = math.pi
    e = math.e
    lognormal_Y={}
    lognormal_X=[]

    for i in range(adet):
        rnd = random.randint (1,adet)
        a = (-1 * (math.log(rnd) - ortalama) ** 2) / (2 * std ** 2)
        r = (1 / (std * rnd * (2 * pi) ** .5)) * e ** (a)
        #print(i, ". ", rnd, "---", r)
        lognormal_Y[rnd]=r
#        lognormal_X.append(rnd)
    return lognormal_Y

Y =Lognormal(100000,15,3)
#Y=Normal(10000,15,3)
X=sorted(Y.keys())

Y_axis=[]
for i in X:
    Y_axis.append(Y[i])
plt.figure()
plt.plot(X, Y_axis)
plt.xlabel(' X ')
plt.ylabel(' Y ')
plt.title(' Lognormal')
plt.show()
