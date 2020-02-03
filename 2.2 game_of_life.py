import matplotlib
matplotlib.use('TkAgg')
from pylab import *

n = 100 # size of space: n x n
p = 0.1 # probability of initially alive cells

def density_setter(val = p):
    '''
    Probability of a cell being alive
    '''
    global p
    p = float(val)
    return val

def get_density(config):
    return sum(config) / config.size

def initialize():
    global config, nextconfig, densities
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    densities = [get_density(config)]
    
def observe():
    global config, nextconfig
    densities.append(get_density(config))
    cla()
    subplot(1,2,1)
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)
    subplot(1,2,2)
    plot(range(len(densities)), densities)

def update():
    global config, nextconfig
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
                
            count -= config[x, y]
            if (config[x, y] == 1 and 2 <= count <= 3) or (config[x, y] == 0 and count == 3):
                nextconfig[x, y] = 1
            else:
                nextconfig[x, y] = 0

    config, nextconfig = nextconfig, config

import pycxsimulator
pycxsimulator.GUI(parameterSetters=[density_setter]).start(func=[initialize, observe, update])
