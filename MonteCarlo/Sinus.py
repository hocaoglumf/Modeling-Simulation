import random
import math
import matplotlib.pyplot as plt

x=[]
y=[]
i=0
points=[]
pointY=[]
while (i<math.pi/2):
    x.append(i)
    y.append(math.sin(i))
    if (random.randint(0,10)>6):
        rndY = random.randint(0,1000)/1000
        rndX= random.randint(0,int(math.pi/2*1000))/1000
        points.append(rndX)
        pointY.append(rndY)
    i+=0.001





plt.figure()
plt.plot(x, y)
plt.xlabel(' X ')
plt.ylabel(' Y ')
plt.title(' Sinus ')

for i in range(len(points)):
    plt.plot(points[i], pointY[i], 'g.')


plt.show()