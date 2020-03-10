import matplotlib
from pylab import *
import networkx as nx
import random as rd

p_i = 0.5  # infection probability
p_r = 0.5  # recovery probability

def initialize():
    global g
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < .5 else 0

def observe():
    global g
    cla()
    nx.draw(g, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            pos = g.pos)

def update():
    global g
    next_g = g.copy()
    all_nodes = list(g.nodes)
    for node_id in all_nodes:
        if g.nodes[node_id]['state'] == 0:  # if susceptible
            all_neighbors = list(g.neighbors(node_id))
            infected_neighbors = 0
            for neighbor in all_neighbors:
                if neighbor['state'] == 1:  
                    infected_neighbors += 1
            infection_chance = p_i * (1 - (1-p_i)**(infected_neighbors+1)) / (p_i)
            next_g[node_id]['state'] = 1 if random.random() < infection_chance else 0
        else:  # if infected
            g.nodes[node_id]['state'] = 0 if rd.random() < p_r else 1

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])