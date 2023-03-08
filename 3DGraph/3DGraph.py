import numpy as np
import matplotlib.pyplot as plt

def f1(x,y):
    return 1/3*(x**2+(y-1)**2)
def f2(x,y):
    return 1/3*(x-1)**2+y**2+2
def f3(x,y):
    return 1/3*(x**2+(y+1)**2+1)

def ft(x,y):
    return 1/3*(f1(x,y)+f2(x,y) + f3(x,y))
xline=[]
yline=[]
zline1=[]
zline2=[]
zline3=[]
zlinet=[]
n0 =-200
n1=200
step=1
for x in range(n0,n1, step):
    for y in range(n0,n1, step):
        xline.append(x/100)
        yline.append(y/100)
        zline1.append(f1(x/100,y/100))

for x in range(n0,n1, step):
    for y in range(n0,n1, step):
        zline2.append(f2(x/100,y/100))

for x in range(n0,n1, step):
    for y in range(n0,n1, step):
        zline3.append(f3(x/100,y/100))

for x in range(n0,n1, step):
    for y in range(n0,n1, step):
        zlinet.append(ft(x/100,y/100))

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(xline, yline, zline1, 'gray')
ax.plot3D(xline, yline, zline2, 'red')
ax.plot3D(xline, yline, zline3, 'green')
#ax.plot3D(xline, yline, zlinet, 'blue')


plt.show()


