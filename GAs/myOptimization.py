import random

class Crossover:
    def __init__(self):
        pass
    def Crossover(self, x, C0, C1):
        c0b=C0[0:x]
        c1b=C1[0:x]
        c0s=C0[x:len(C0)]
        c1s=C1[x:len(C1)]
        cn0=Chromosome()
        cn0.chromosome= c0b+c1s
        cn1=Chromosome()
        cn1.chromosome= c1b+c0s

class Chromosome:
    def __init__(self):
        self.chromosome=""

    def First(self):
        for i in range(44):
            r=random.random()
            g=0
            if (r<=0.5):
                g=1
            self.chromosome +=str(g)


