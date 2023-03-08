class Musteri():
    def __init__(self, id):
        self.id=id

class Kasa():
    def __init__(self,id, serviceDuration):
        self.id=id
        self.kuyruk=[]
        self.inService=None
        self.t=0
        self.serviceT=0
        self.ServisSuresi=serviceDuration

    def ServisSuresi(self,s):
        self.ServisSuresi=s

    def Service(self,m):
        self.inService=m

    def AddQueue(self,m):
        self.kuyruk.append(m)

    def SelectCustomer(self):
        if (self.Available()):
            self.inService= self.kuyruk[0]
            self.kuyruk.pop(0)
            self.serviceT=0

    def Lq(self):
        return len(self.kuyruk)

    def Available(self):
        return self.inService==None

    def Process(self,deltaT):
        self.t +=deltaT
        if (self.Available()==False):
            self.serviceT +=deltaT
            if (self.serviceT % self.ServisSuresi ==0):
                print("Zaman :", self.t, " müşteri ", self.inService.id, " kuyruktan ayrıldı ", self.id, " kuyruk uzunluğu ", self.Lq())
                self.inService=None
                #input("..")
        if (self.Lq()>0):
            self.SelectCustomer()

class Simulation():
    def __init__(self):
        self.Gelisler=3
        self.t=0
        self.kasalar=[]
        self.kasalar.append(Kasa(1,5))
        self.kasalar.append(Kasa(2,5))

    def GelislerArasiSure(self,g):
        self.Gelisler=g

    def Create(self):
        print("Zaman :",self.t," yeni müşteri girişi.")
        return Musteri(self.t)

    def ShortQueue(self):
        s= self.kasalar[0].Lq()
        k=None
        for i in self.kasalar:
            if (i.Lq()<=s):
                k=i
        return k

    def Process(self, deltaT):
        self.t += deltaT
        for i in self.kasalar:
            i.Process(deltaT)

        if (self.t % self.Gelisler ==0):
            m=self.Create()
            b=False
            for i in self.kasalar:
                if (i.Available()):
                    i.inService = m
                    b=True
                    break
            if (b==False):
                q=self.ShortQueue()
                q.AddQueue(m)
        return self.t

deltaT = 1
s=Simulation()

sure= int (input("Koşum Süresi :"))
while True:
    T= s.Process(deltaT)
    if (T>=sure):
        print(" Elveda Zalim Dünya ..")
        break
