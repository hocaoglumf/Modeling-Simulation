import random

class Cell:
    def __init__(self, x, y,state):
        self.x=x
        self.y=y
        self.state=state

    def SetState(self, state):
        self.state =state


class World:
    def __init__(self, m, n):
        self.world=[]
        self.Create(m,n)

    def Create(self, m, n):
        for i in range(m):
            for j in range(n):
                state=0
                if random.randint(0,100)<=50:
                    state=1
                self.world.append(Cell(i,j,state))


w=World(100,100)

for i in range(1000):
    

