import matplotlib.pyplot as plt
from BouncingBall import BouncingBall_2OOP
import random


class TopSimulasyonu():
    def __init__(self, n):
        self.toplar = []
        self.CreateBalls(n)
        self.deltaT =0.01

    def CreateBalls(self,n):
        for i in range(topSayisi):
            self.toplar.append(BouncingBall_2OOP.Top(i, random.randint(1, 20), 0))

    def Run(self):
        while (True):
            tpl = 0
            for i in self.toplar:
                hmax,h = i.Process()
                tpl += hmax
                print(i.id, "  ", hmax, "  ", h)
            if (tpl == 0):
                break
            print("-----------")
        self.Plot()

    def Plot(self):
        plt.figure()
        for i in self.toplar:
            plt.plot(i.T, i.H)
        plt.xlabel('Zaman')
        plt.ylabel('Yükseklik')
        plt.title('Zıplayan Top')
        plt.show()

topSayisi= int(input("Top Sayısı :"))

S=TopSimulasyonu(topSayisi)
S.Run()





