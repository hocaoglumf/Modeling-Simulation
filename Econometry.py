import matplotlib.pyplot as plt
C=float(input("Tüketim :"))
I=float(input("Yatırım :"))
T=float(input("Vergiler :"))
G=float(input("Hükümet masrafları :"))
N=float(input("Milli gelir:"))

t=0
time=[]
CL=[]
TL=[]
IL=[]
NL=[]
while (True):
    if t>100:
        break
    t +=1
    C= 30 + 0.8 * (N -T)
    I=3 + 0.2 *N
    N= C + I + G
    T= 0.3 * N
    print (round(t,3), "C: ", round(C,3), "N: ", round(N,3), "I: ", round(I,3), "T: ", round(T,3))
    time.append(t)
    CL.append(C)
    IL.append(I)
    NL.append(N)
    TL.append(T)

plt.title("Ekonometri Modeli")
plt.xlabel("Zaman ")

plt.plot(time,CL, label="Tüketim")
plt.plot(time,IL, label="Yatırım")
plt.plot(time,NL, label="Milli Gelir")
plt.plot(time,TL, label="Vergiler")
plt.legend()
plt.show()
