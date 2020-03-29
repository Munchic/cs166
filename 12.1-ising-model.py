import random
import copy

import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import numpy as np


n = 10  # size of space: n x n
p = 0.5  # probability of positive
t = 1  # unitless temperature 
avg_magns = []  # list to store average magnetization over time steps

def temp_setter(val=t):
    '''
    Temperature of the system
    '''
    global t
    t = float(val)
    return val

def calc_avg_magn(config):
    n = config[0].size
    avg_magn = np.sum(config) / n**2 

    return avg_magn

def initialize():
    global config, avg_magns
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else -1

    avg_magns.append(calc_avg_magn(config))
    

def observe():
    global config
    avg_magns.append(calc_avg_magn(config))

    cla()
    subplot(1,2,1)
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)

    subplot(1,2,2)
    plt.ylim((-1, 1))
    plt.title('average magnetization')
    plt.xlabel('step')
    plot(range(len(avg_magns)), avg_magns)

def update():
    global config, t, step

    x = randint(0, n - 1)
    y = randint(0, n - 1)

    energy = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            # check for von-Neumann neighborhood:
            if abs(dx) * abs(dy) == 0:
                energy += config[(x + dx) % n, (y + dy) % n]  
    energy *= -config[x, y]  # product with central cell
    
    if random() < min(1, e**(2*energy / t)):
        config[x, y] = -config[x, y]
    avg_magns.append(calc_avg_magn(config))

import pycxsimulator
pycxsimulator.GUI(parameterSetters=[temp_setter]).start(func=[initialize, observe, update])
