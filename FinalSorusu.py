import numpy
import random

class Customer:
    def __init__(self, no, d):
        self.no=no
        self.serviceDuration=-1
        self.entranceTime=d
        self.exitTime=999999999999999999999999999


class Service:
    def __init__(self, service):
        self.service=service
        self.queue=[]
        self.T=0
        self.entityBeingProcessed=None

    def ServiceDuraiton(self):
        return numpy.random.exponential(self.service)

    def Attach(self, s):
        serviceDur=self.ServiceDuraiton()
        s.serviceDuration=serviceDur
        self.queue.append(s)

    def SetTime(self,T):
        self.T=T

    def ExitTime(self):
        if (self.entityBeingProcessed == None):
            return 999999999999999
        else:
            return self.entityBeingProcessed.exitTime


s1=Service(10)
s2=Service(14)


musteriler=[]
R=0
def Normal(nu, std):
    nr=0
    for i in range(12):
        nr += random.randint(0,100)/100

    nr = nr -6
    return 8+nr*std

for i in range(1000):
    d=Normal(8,  1)
    R +=d
    musteriler.append(Customer(i,R))

def FindMinTime():
    min =0
    tip=-1
    if (musteriler[0].entranceTime <= s1.ExitTime()):
        min = musteriler[0].entranceTime
        tip=0
    else:
        min = s1.ExitTime()
        tip=1

    if (min >=s2.ExitTime()):
        min = s2.ExitTime()
        tip=2

    return min, tip
T=0
Time=0
print ("Time ", "S1 kuyruk    S1 işlem   S1 Çıkış   S2 Kuyruk  S2 işlem S2 Çıkış")
while True:
    T,tip = FindMinTime()
    Time = T
    if (tip == 0):
        c = musteriler[0]
        if (len(s1.queue)<=len(s2.queue) ):
            if (s1.entityBeingProcessed == None):
                if (c.serviceDuration==-1):
                    c.serviceDuration=s1.ServiceDuraiton()
                c.exitTime = Time + c.serviceDuration
                s1.entityBeingProcessed = c
                print (round(Time,2), "                 ", c.no, )
            else:
                s1.Attach(c)
                print(round(Time,2), "   ",c.no, "")
        else:
            if (s2.entityBeingProcessed == None):
                if (c.serviceDuration==-1):
                    c.serviceDuration=s2.ServiceDuraiton()
                c.exitTime = Time + c.serviceDuration
                print (round(Time,2), "                                                 ", c.no, )
                s2.entityBeingProcessed = c
            else:
                s2.Attach(c)
                print(round(Time,2), "                                                          ", c.no, "")
        musteriler.pop(0)
    elif (tip==1):
        print(round(Time, 2), "                         ", s1.entityBeingProcessed.no)
        s1.entityBeingProcessed = None

        if (len(s1.queue)>0):
            c = s1.queue[0]
            s1.entityBeingProcessed = c
            c.exitTime = Time + c.serviceDuration
            s1.queue.pop(0)
            print(round(Time, 2), "                 ", c.no, )
    elif (tip==2):
        s2.entityBeingProcessed = None
        if (len(s2.queue)>0):
            c = s2.queue[0]
            c.exitTime = Time + c.serviceDuration
            s2.entityBeingProcessed = c
            s2.queue.pop(0)
            print(round(Time, 2), "                                                       ", c.no, )

