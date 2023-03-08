import random
import math
x=-1
for i in range(0,10):
    rn = random.randint(0, 100) / 100
    if (rn>=0 and rn<0.2):
        x=math.log10(rn*100+5)
    elif (rn >= 0.2 and rn < 0.5):
        x = 2
    elif (rn >= 0.5 and rn < 0.7):
        x = math.e**(rn*10)
    elif (rn >= 0.7 and rn < 0.8):
        x = 4
    else:
        x=112
    print(x)


