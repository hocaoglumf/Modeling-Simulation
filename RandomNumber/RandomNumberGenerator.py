import random
def RandomNumberGenerator(adet):
    R=[]
    Y=[]
    YY=[]
    x=0
    for i in range(adet):
        x+=1
        R.append(random.randint(0,100)/100)
        Y.append(x)
        YY.append(0.5)
    return R, Y, YY
