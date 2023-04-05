import time
import datetime
class Call:
    def __init__(self, type):
        self.duration=0
        self.type=type
        self.priority=0

    def Consume(self,t):
        self.duration -=t
        return self.duration

class Operator:
    def __init__(self, dur):
        self.duration=dur
        self.service=None
        self.queue=[]

    def Serve(self):
        if len(self.queue)>0:
            self.service=self.queue.pop(0)
        else:
            self.service=None

    def Sort(self):
        for i in range(len(self.queue)-1):
            for j in range(i,len(self.queue)):
                f0=self.queue[i]
                f1=self.queue[j]
                if (f0.priority >= f1.priority):
                    f0,f1=f1,f0

    def PutQueue(self, q):
        q.duration=self.duration
        self.queue.append(q)
        self.Sort()
        if self.service==None:
            self.Serve()

    def ConsumeTime(self,t):
        if self.service==None:
            return None
        resume=self.service.Consume(t)
        r=self.service
        if resume ==0:
            self.Serve()
            return r
        return None

class CallGenerator:
    def Generate(self,t):
        x=None
        y=None
        if (t % 5 == 0):
            x= Call("x"+str(t))
            x.priority=2
            print("Zaman:", t, " ",x.type, "  geldi.")
        if (t % 10==0):
            y=Call("y"+str(t))
            y.priority=1
            print("Zaman:", t, " ", y.type, "  geldi.")
        return x,y

cagriYonDur=int(input("Çağrı Yönlendirme Süresi: "))
operator1Dur=int(input("Operatör -1 Servis Süresi: "))
operator2Dur=int(input("Operatör -2 Servis Süresi: "))
simDuration=int(input("Koşum Uzunluğu :"))
simSpeed=int(input("İşletim Hızı (-1 as fast as):"))

gen=CallGenerator()
cagriYon=Operator(cagriYonDur)
operator1=Operator(operator1Dur)
operator2=Operator(operator2Dur)

t=0
dt=1
first_time = datetime.datetime.now()
while True:
    if simDuration<=t:
        later_time = datetime.datetime.now()
        difference = later_time - first_time
        print ("Geçen süre :", difference)
        tt=difference.total_seconds()
        if tt>0:
            print("Hız : ", simDuration/tt)
        print("Elveda Zalim Dünya...")
        break
    t +=dt

    if (simSpeed>0):
        time.sleep(dt/simSpeed)
    r=cagriYon.ConsumeTime(dt)
    r1=operator1.ConsumeTime(dt)
    r2=operator2.ConsumeTime(dt)
    if (not(r1==None)):
        print("Zaman:", t, " ",r1.type, " ayrılıyor.")

    if (not(r2==None)):
        print("Zaman:", t, " ",r2.type, " ayrılıyor.")

    x,y=gen.Generate(t)
    if (not(x ==None)):
        cagriYon.PutQueue(x)
    if (not(y ==None)):
        cagriYon.PutQueue(y)

    if not(r==None):
        if r.type[0]=="x":
            operator1.PutQueue(r)
            print ("Zaman : ", t, "  ", r.type, "-->  operatör-1 Kuyruk:", len(operator1.queue))
        elif r.type[0]=="y":
            operator2.PutQueue(r)
            print ("Zaman : ", t, "  ", r.type, "-->  operatör-2 Kuyru:", len(operator2.queue))
