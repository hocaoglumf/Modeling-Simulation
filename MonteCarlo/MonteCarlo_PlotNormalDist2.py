import math
from matplotlib import pyplot
import random
def Sort(x,y):
    for i in range(len(x)-1):
        for j in range(i,len(x)):
            if (x[i]>x[j]):
                x[i],x[j]=x[j],x[i]
                y[i],y[j]=y[j],y[i]
    return x,y

def normpdf(mean, sd, N):
    xl=[]
    nrp=[]
    for i in range(N):
        x=random.randint (-5000,5000)/1000
        var = float(sd)**2
        denom = sd*(2*math.pi)**.5
        num = math.exp(-0.5*((x-mean)/sd)**2)
        xl.append(x)
        nrp.append(num/denom)
    return Sort(xl, nrp)
# Dağılımın tanımı
mu = 0
sigma = 1
sizes = [1000]
for i in range(len(sizes)):
    X,Y = normpdf(mu, sigma, sizes[i])
    pyplot.plot(X,Y)
# Örnek histogram çizimi
pyplot.show()