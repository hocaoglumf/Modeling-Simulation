import math
import matplotlib.pyplot as plt
import RungeKutta as RK

def f(t, q):
    return 9* (.2 *(1+math.cos(t))) - 6*(q/(600+3*t))

# Girdiler
print('Başlangıç durumu girişi:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Hesaplama noktası girişi: ')
xn = float(input('xn = '))

print('Adım sayısı girişi:')
step = int(input('Adım Sayısı = '))

x,y=RK.rk4(x0, y0, xn, step, f)
plt.plot(x,y)
plt.show()