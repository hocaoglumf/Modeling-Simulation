'''
c = 0.767 - 3.36/lambda
beta = PI/sqrt(3.0*lambda)
alpha = beta*lambda
k = log(c) - lambda - log(beta)

forever
{
	u = random()
	x = (alpha - log((1.0 - u)/u))/beta
	n = floor(x + 0.5)
	if (n < 0)
		continue
	v = random()
	y = alpha - beta*x
	lhs = y + log(v/(1.0 + exp(y))^2)
	rhs = k + n*log(lambda) - log(n!)
	if (lhs <= rhs)
		return n
}
'''
import math
import random

def Factorial(N):
    if (N==0):
        return 1
    return N*Factorial(N-1)

def RandomValue(alpha, lmbd):
    while (True):
        u = random.random()
        x = (alpha - math.log((1.0 - u) / u)) / beta
        n = math.floor(x + 0.5)
        if (n < 0):
            continue
        v = random.random()
        y = alpha - beta * x
        lhs = y + math.log(v / (1.0 + math.exp(y)) ** 2)
        rhs = k + n * math.log(lmbd ) - math.log(Factorial(n))
        if (lhs <= rhs):
            return n

N=int(input("Kaç Adet Rastsal Değer Üretilecek :"))
lmbd=float(input("Lambda değeri : "))

c = 0.767 - 3.36/lmbd
beta = math.pi/(3.0*lmbd)**.5
alpha = beta*lmbd
k = math.log(c) - lmbd - math.log(beta)
randomPoisson=[]
for i in range (0,N):
    randomPoisson.append(RandomValue(alpha,lmbd))

print(randomPoisson)