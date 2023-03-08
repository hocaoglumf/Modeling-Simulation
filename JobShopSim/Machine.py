import PetriNets.SimulationEntity
import PetriNets.Petri


class Machine(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None


    def Initialize(self):
        ''' Common data '''
        eventGuards = {"t0": "null", "t1": "null"}
        exitFunctions = {"t0": "null", "t1": "Meth0"}
        timeGrantFunctions={"t0": "null", "t1": "Meth1"}
        state0 = {"P0": 0, "P1": 1, "P2": 0, "P3": 0}
        eventPriority = {"t0": PetriNets.Petri.Transition(1), "t1": PetriNets.Petri.Transition(1)}
        transitionMatrix0 = [[-1, -1, 1, 0],
                             [0, 1, -1, 1]]
        transitionMatrix1 = [[0, 0, 0, 0],
                             [0, 0, 0, 0]]
        ''' Machine-0 private data '''
        petri= PetriNets.Petri.PetriNet()
        self.SetPetri(petri)
        self.petri.SetTimeGrantFunctions(timeGrantFunctions)
        self.petri.SetExitFunctions(exitFunctions)
        self.petri.SetGuards(eventGuards)
        self.petri.SetTransitionMatrix(transitionMatrix0, transitionMatrix1)
        self.petri.SetState(state0)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)
        self.factoryRef = globals()['Machine']()

    def Meth0(self):
        return True

    def Meth1(self):
        return True


