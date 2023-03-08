#h0 = 5         # m/s
#v = 0          # m/s, mevcut hız
#g = 10         # m/s/s
#t = 0          # başlama zamanı
#dt = 0.001     # zaman adımı
#rho = 0.75     # Geri sıçrama katsayısı
#tau = 0.10     # zıplama etkileşim süresi
#hmax = h0      # Maksimum yükseklik kontrolü
#h = h0
#hstop = 0.01   # zıplama kontrol yüksekliği
#freefall = True # Durum: serbest düşme veya sıçrama sonrası hareket (True) veya çarpma etkileşiminde (False)
#t_last = -sqrt(2*h0/g) # h0'a ulaşacağımız zaman

from math import sqrt
import math
import random
class Top():
    def __init__(self,id, h, v):
        self.id=id
        self.h=h
        self.v=v
        self.g=10
        self.t=0
        self.freefall=True
        self.t_last = -sqrt(2*self.h/self.g)
        self.hmax =h
        self.vmax =sqrt(2 * self.hmax * self.g)
        self.rho = 0.75  # Geri sekme katsayısı (coefficient of restitution)
        self.tau = 0.0010
        self.dt=0.01
        self.T=[]
        self.H=[]



    def FreeFall(self):
        hnew = self.h + self.v*self.dt - 0.5*self.g*self.dt**2
        if(hnew<0):
          self.t = self.t_last + 2*sqrt(2*self.hmax/self.g)
          self.freefall = False
          self.t_last = self.t + self.tau
        else:
          self.t = self.t + self.dt
          self.v = self.v - self.g*self.dt
          self.h = hnew
        print("id: ", self.id, "  h: ", round(self.h,2), "  v: ", round(self.v,3))
        return self.h

    def Bouncing(self):
        self.t = self.t + self.tau
        self.vmax = self.vmax * self.rho
        self.v = self.vmax
        self.freefall = True
        self.h = 0
      #  self.FreeFall(self.dt-self.tau)
        return self.h

    def isFreeFall(self):
        return self.freefall

    def isBouncing(self):
        return not(self.freefall)

    def Process(self):
        h=0
        if (self.freefall):
            h=self.FreeFall()
        else:
            h=self.Bouncing()

        self.hmax = 0.5 * self.vmax ** 2/ self.g
        self.H.append(h)
        self.T.append(self.t)
        return self.hmax,h

