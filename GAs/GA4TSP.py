import random

cities=[1,2,3,4,5,6,7,8,9,"A"]
distances=[[20,30,10,40,90]]
class Chromosome:
    def __init__(self,N=5):
        self.chromosome=""
        self.length=N
        self.weight=-1
        self.Create()

    def Create(self):
        citiesSave =[]
        for i in cities:
            citiesSave.append(i)

        for i in range(self.length):
            length = len(citiesSave)
            rnd=random.randint(0,length-1)
            gene=citiesSave[rnd]
            citiesSave.pop(rnd)

            self.chromosome += str(gene)


    def SetChromosome(self,c, mr):
        self.chromosome=c
        self.Mutation(mr)

    def isValid(self):
        totalW=0
        for i in range(len(self.chromosome)):
            totalW += knapsak[i].weight* int(self.chromosome[i])
        self.weight = totalW
        cpcty=capacity[0]
        return totalW<=cpcty

    def Mutation(self,mr):
        mutate = random.randint(0, 100)
        wh=-1
        if (mutate <= mr*100):
            xx=len(knapsak)-1
            wh = random.randint(0, xx)
        if (wh >-1):
            c=list(self.chromosome)
            gene = int(c[wh])
            gene = (gene +1)%2
            c[wh]=str(gene)
            self.chromosome=""
            for i in c:
                self.chromosome +=str(i)


    def Fitness(self):
        totalV = 0
        for i in range(len(self.chromosome)):
            totalV += knapsak[i].value * int(self.chromosome[i])
        return totalV




class Pool:
    def __init__(self,mr=.03):
        self.pool=[]
        self.mutationRate=mr

    def Initial(self,N):
        x=len(self.pool)
        chrLen = len(knapsak)
        while (N>x):
            self.Attach(Chromosome(chrLen ))
            x = len(self.pool)

    def Attach(self,c):
        if (c.isValid()):
            self.pool.append(c)

    def Crossover(self):
        pool1=[]
        pool2=[]
        k=1
        for i in self.pool:
           if (k%2==0):
               pool1.append(i)
           else:
               pool2.append(i)
           k +=1
        k=0
        for i in pool1:
            xx=len(knapsak)-1
            crs=random.randint(1,xx)
            firstFirst=i.chromosome[:crs]
            firstSecond=i.chromosome[crs:]

            secondFirst=pool2[k].chromosome[:crs]
            secondSecond=pool2[k].chromosome[crs:]

            child1=firstFirst+secondSecond
            child2=secondFirst+firstSecond
            N=len(knapsak)
            a=Chromosome(N)
            a.SetChromosome(child1, self.mutationRate)
            self.Attach(a)
            b=Chromosome(N)
            b.SetChromosome(child2, self.mutationRate)
            self.Attach(b)

    def KillTheWorstOnes(self,N):
        # En kötü fitness değerine sahip
        # kromozomları siler
        i=0

        while (i<=N-1):
            toDie=self.MinFitness()
            i +=1
            self.pool.remove(toDie)

    def RouletteWheelSelection(self,N):
        sum_of_fitness =0
        for c in self.pool:
            sum_of_fitness  += c.Fitness()

        previous_probability = 0.0

        wheel=[]
        for i in self.pool:
            previous_probability  = previous_probability + (i.Fitness() / sum_of_fitness)
            wheel.append(previous_probability)

        rnd=random.randint(0,100)/100
        toBeRemoved=[]
        for i in range(len(wheel)-1):
            ckr=0
            if (i>0):
                ckr =0#wheel[i-1]

            if (rnd <= wheel[i]-ckr):
                toBeRemoved.append(self.pool[i])

        for i in toBeRemoved:
            self.pool.remove(i)



    def Kill(self,N,selection=0):
        if (selection ==0):
            self.KillTheWorstOnes(N)
        elif (selection==1):
            self.RouletteWheelSelection(N)

    def MaxFitness(self):
        mx=self.pool[0].Fitness()
        mxC=self.pool[0]
        for i in self.pool:
            if (mx <= i.Fitness()):
                mxC=i
        return mxC

    def MinFitness(self):
        mn=self.pool[0].Fitness()
        mnC=self.pool[0]
        for i in self.pool:
            if (mn >= i.Fitness()):
                mnC=i
        return mnC


#Problem Çözümü
# Item (Value, Weight)
#knapsak=[Item(4,12), Item(2,2), Item(2,1), Item(1,1), Item(10,4)]
#capacity=[15]
knapsak=[Item(4,12), Item(2,2), Item(2,1), Item(1,1), Item(10,4),
         Item(8,1), Item(9,3), Item(6,2), Item(7,5)]
capacity=[25]

Population =100
pool=Pool()
pool.Initial(Population )
iteration =0

while (True):
    iteration +=1
    pool.Crossover()
    pool.Kill(len(pool.pool)-Population, 0 )
    mxc= pool.MaxFitness()
    print("iterasyon:",iteration, "  ",mxc.chromosome, " Değer: ", mxc.Fitness(), " Ağırlık: ", mxc.weight)
    oldChr= mxc.chromosome
