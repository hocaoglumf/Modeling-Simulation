
import random
import math
lmb = 0.5

def Exp_RND(lmb):
    rnd = -1.0/lmb*math.log(1-random.random())
    return rnd
'''
for i in [1,2,3,4,5]:
    for j in range(0,10):
        print(Exp_RND(2*i)*10)
    print("------------")
'''