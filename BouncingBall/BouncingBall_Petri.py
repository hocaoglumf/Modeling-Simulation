from PetriNets import Petri

from BouncingBall import BouncingBall_2OOP

global ball,bouncing,freeFall, isbouncing,isfreefall
ball= BouncingBall_2OOP.Top(1, 20, 0)
bouncing = getattr(BouncingBall_2OOP.Top, 'Bouncing')
freeFall = getattr(BouncingBall_2OOP.Top, 'FreeFall')
isfreefall = getattr(BouncingBall_2OOP.Top, 'isFreeFall')
isbouncing = getattr(BouncingBall_2OOP.Top, 'isBouncing')

#sxx = "bouncing(ball)"
#x=eval(sxx)
#print(x)
#bouncing(ball)



transitionDurationCalculation ={"t0":-1, "t1":0.01,"t2":0.001}
state=[1,0]
eventPriority={"t0":1, "t1":1, "t2":1}

transitionMatrix1=[
                  [-1, 1],
                  [1,-1],
                  [1, -1]]

guards={"t1":"BouncingBall_2OOP.isfreefall(ball)", "t2":"BouncingBall_2OOP.isbouncing(ball)"}
functions={"t1":"BouncingBall_2OOP.freeFall(ball)", "t2":"BouncingBall_2OOP.bouncing(ball)"}

pn= Petri.PetriNet()
pn.SetGuards(guards)
pn.SetFunctions(functions)
pn.SetTransitionDurationCalculation(transitionDurationCalculation)
pn.SetTransitionMatrix([],transitionMatrix1)
pn.SetState(state)
pn.SetSimulationDuration(5000)
pn.SetEventPriority(eventPriority)
pn.Simulate()
