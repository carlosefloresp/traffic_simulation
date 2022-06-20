import random

import car_following
from threading import *
from time import *


class Simulation(Thread):
    def __init__(self, id):
        self.id = id
        self.rand_int = -1

    def slow_function(self, name):
        sleep(1.0)
        self.rand_int = random.randint(0, 10)
        print("      thread " + str(name) + " rand to send: " + str(self.rand_int))


class HMI(Thread):
    def __init__(self, id):
        self.id = id

    def slow_function(self, name, i):
        print("      thread "+ str(name) + " received: " + str(i))
        sleep(1.0)

simulation = Simulation(0)
hmi = HMI(1)


for i in range(4):
    t1 = Thread(target=simulation.slow_function, args=("alpha",))
    t2 = Thread(target=hmi.slow_function, args=("beta", simulation.rand_int))
    t1.start()
    t2.start()

    t1.join()
    t2.join()


# Init vehicles with random models, with probability of selecting a model type

# Init them at random positions and half of the speed limit

# Link each vehicle with its preceding and following

#### Loop

# create a copy of current vehicle states

# compute actions and update vehicle states

# 