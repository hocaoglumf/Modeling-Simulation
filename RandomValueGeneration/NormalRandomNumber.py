import random

def NormalRandomNumber(N):
    t=0
    for i in range(N):
       t = t + random.random()
    return (t-N/6)/(N/12)

