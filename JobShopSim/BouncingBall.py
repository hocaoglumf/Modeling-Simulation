import PetriNets.SimulationEntity
import PetriNets.Petri
import random
import math
class Ball(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None
        self.h=random.randint(1,10)
        self.v=random.randint(0,10)
        self.g=10
        self.t=0
        self.freefall=True
        self.t_last = - math.sqrt(2*self.h/self.g)
        self.hmax =self.h
        self.vmax =math.sqrt(2 * self.hmax * self.g)
        self.rho = 0.75  # Geri sekme katsayısı (coefficient of restitution)
        #self.dt=0.01
        self.T=[]
        self.H=[]

    def Initialize(self):
        transitionGuards = {"t0": "null", "t1": "null", "t2":"isFreeFall", "t3":"isBouncing", "t4":"null", "t5":"Stop"}
        timeGrantFunctions={"t0": "null", "t1": "null", "t2":"null", "t3":"null", "t4":"null", "t5":"null"}
        exitFunctions={"t0": "null", "t1": "FreeFall", "t2":"null", "t3":"null", "t4":"Bouncing", "t5":"null"}

        state0 = {"P0": 1, "P1": 1, "P2": 0, "P3": 0,"P4":0, "P5":0}
        eventPriority = {"t0": PetriNets.Petri.Transition(1), "t1": PetriNets.Petri.Transition(1)}
        transitionMatrix0 = [[-1, -1, 1, 0, 0, 0],
                             [ 0,  0,-1, 1, 0, 0],
                             [ 1,1,0,-1,0,0],
                             [0,0,0,-1,1,0],
                             [1,1,0,0,-1,0],
                             [0,0,0,-1,0,1]]

        transitionMatrix1 = []
        for i in range(6):
            s=[]
            for j in range (6):
                s.append(0)
            transitionMatrix1.append(s)

        petri= PetriNets.Petri.PetriNet()
        self.SetPetri(petri)
        self.petri.SetGuards(transitionGuards)
        self.petri.SetTimeGrantFunctions(timeGrantFunctions)
        self.petri.SetExitFunctions(exitFunctions)
        self.petri.SetTransitionMatrix(transitionMatrix0, transitionMatrix1)
        self.petri.SetState(state0)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)

        self.factoryRef = globals()['Ball']()

    def FreeFall(self,dt):
        hnew = self.h + self.v*dt - 0.5*self.g*dt**2
        if(hnew<0):
          self.t = self.t_last + 2*math.sqrt(2*self.hmax/self.g)
          self.freefall = False
          #self.t_last = self.t + self.tau
        else:
          self.t = self.t + dt
          self.v = self.v - self.g*dt
          self.h = hnew
        print("  h: ", round(self.h,2), "  v: ", round(self.v,3))
        return self.h

    def Bouncing(self, tau):
        self.t = self.t + tau
        self.vmax = self.vmax * self.rho
        self.v = self.vmax
        self.freefall = True
        self.h = 0

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

    def Stop(self):
        return self.h <=0.0001 and abs(self.v)<0.0001

