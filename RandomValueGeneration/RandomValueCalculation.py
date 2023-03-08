import random
from RandomValueGeneration import ExplonentionalRandomNumber


def Uniform(b,a):
    return (b-a)*random.random() +a

def Constant(x):
    return x

def Normal(Mean,Std):
    sum=0
    for i in range(12):
        sum +=random.random()
    rnd = sum-6
    return Mean + rnd *Std

def Exponential(lmbd):
    return ExplonentionalRandomNumber.Exp_RND(lmbd)


