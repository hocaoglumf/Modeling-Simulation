# Runge Kutta -4 metot
x=[]
y=[]
def rk4(x0, y0, xn, n, func):
    # Adım genişliği hesaplama
    h = (xn - x0) / n
    print('\n--------Çözüm--------')
    print('-------------------------')
    print('x0\ty0\tyn')
    print('-------------------------')
    for i in range(n):
        k1 = h * (func(x0, y0))
        k2 = h * (func((x0 + h / 2), (y0 + k1 / 2)))
        k3 = h * (func((x0 + h / 2), (y0 + k2 / 2)))
        k4 = h * (func((x0 + h), (y0 + k3)))
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f' % (x0, y0, yn))
        print('-------------------------')
        y0 = yn
        x0 = x0 + h
        x.append(x0)
        y.append(y0)
    print(' x=%.4f, y=%.4f' % (xn, yn))
    return x,y
# RK4 çözüm için çağrılır: rk4(x0, y0, xn, step, func)