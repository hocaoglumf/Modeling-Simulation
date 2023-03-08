import random
randomNumbers=[]
for i in range(0,300):
    x=random.randint(0,100)
    randomNumbers.append(x/100)
    print("between", 0, " and ", 100,"  random number ",x/100)

print(randomNumbers)