import math
import random
xu = float(input(" x ust sınır"))
xa = float(input(" x alt sınır "))
yu = float(input(" y ust sınır "))
ya = float(input(" y alt sınır "))

def Function(x,y):
    return math.sin(x)**math.cos(y) + math.tan(y)**math.sin(x)

za = Function(xa,ya)
zu = Function(xu,yu)
print("z ",za, " ", zu)
v = (zu-za)*(xu-xa)*(yu-ya)
inFun=0
outFun=0
for r in range(0, 200000):
    xr = random.random()*(xu-xa)+xa
    yr = random.random()*(yu-ya)+ya
    zr = Function(xr,yr)
    rz= random.random()*(zu-za)+za
    print(zr, " ", rz)
    if (zr<=rz):
        outFun+=1
    else:
        inFun+=1

print("Under func: ",inFun, " Out of function : ", outFun)
print(v*inFun/(outFun+inFun))

