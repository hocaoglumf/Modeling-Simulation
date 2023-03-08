from p5 import setup, draw, size, background, run
import numpy as np
from boid import Boid

width = 1000
height = 1000

flock = [Boid(*np.random.rand(2)*1000, width, height) for _ in range(30)]

def setup():
    #this happens just once
    size(width, height) #instead of create_canvas



def draw():
    #this happens every time
    background(30, 30, 47)

    for boid in flock:
        boid.show()
