import PetriNets.SimulationEntity
import PetriNets.Petri


class Combiner(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None



    def Initialize(self):
        ''' Common data '''
        eventGuards = {"t0": "null", "t1": "null"}
        #state0 = {"P0": 0, "P1": 0, "P2": 1, "P3": 0, "P4":0}
        eventPriority = {"t0": PetriNets.Petri.Transition(1), "t1": PetriNets.Petri.Transition(1)}
        transitionMatrix0 = [[-5, -4, -1, 1, 0],
                             [ 0,  0,  1,-1, 1]]
        transitionMatrix1 = [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]
        ''' Machine-0 private data '''
        self.petri = PetriNets.Petri.PetriNet()
        self.petri.SetGuards(eventGuards)
        self.petri.SetTimeGrantFunctions(eventGuards)
        self.petri.SetExitFunctions(eventGuards)
        self.petri.SetTransitionMatrix(transitionMatrix0, transitionMatrix1)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)
        self.factoryRef = globals()['Combiner']()

