import random
import math
def Function(x):
    return x**-1

a=1
b=2

N=1000000
sayac=0

for i in range(N):
    rnd=random.random()
    rndab=random.randint(a*100, b*100)/100
    rndf = random.randint(0,100)
    if (Function(rndab)<rndf):
        sayac +=1

print(1*sayac/N)
