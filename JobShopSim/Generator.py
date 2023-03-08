
import PetriNets

class Generator(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None

    def Initialize(self):
        '''Generator'''
        eventGuards = {"t0": "null"}
        state = {"P0": 1, "P1": 0}
        eventPriority = {"t0": PetriNets.Petri.Transition(1)}
        transitionMatrix0 = [[1, 1]]
        transitionMatrix1 = [[-1, 0]]
        self.petri = PetriNets.Petri.PetriNet()
        self.petri .SetGuards(eventGuards)
        self.petri.SetExitFunctions(eventGuards)
        self.petri.SetTimeGrantFunctions(eventGuards)
        self.petri .SetTransitionMatrix(transitionMatrix0, transitionMatrix1)
        self.petri .SetState(state)
        self.petri .SetEventPriority(eventPriority)
        self.petri.SetOwner(self)
        self.factoryRef = globals()['Generator']()

