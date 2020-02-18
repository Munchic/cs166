import matplotlib
# matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd
import numpy as np

def is_homogenous(graph):
    consensus = None
    all_nodes_same = True

    for i in g.nodes:
        if not consensus:
            consensus = g.nodes[i]['state']
        if consensus != g.nodes[i]['state']:
            all_nodes_same = False

    return all_nodes_same

def initialize():
    global g, step_count, tot_steps
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < .5 else 0

    step_count = 0
    tot_steps = None

def observe():
    global g
    cla()
    nx.draw(g, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            pos = g.pos)

def update():
    global g, step_count, tot_steps
    listener = rd.choice(list(g.nodes))
    speaker = rd.choice(list(g.neighbors(listener)))
    g.nodes[listener]['state'] = g.nodes[speaker]['state']

    step_count += 1
    if is_homogenous(g) and not tot_steps:
        tot_steps = step_count
        # print('Reached homogeneity in {} steps'.format(tot_steps))

def update_reverse():
    global g, step_count, tot_steps
    speaker = rd.choice(list(g.nodes))
    listener = rd.choice(list(g.neighbors(speaker)))
    g.nodes[listener]['state'] = g.nodes[speaker]['state']

    step_count += 1
    if is_homogenous(g) and not tot_steps:
        tot_steps = step_count
        # print('Reached homogeneity in {} steps'.format(tot_steps))

def update_edge_based():
    global g, step_count, tot_steps
    edge = rd.choice(list(g.edges))
    idx = rd.randint(0, 1)
    listener = edge[idx]
    speaker = edge[abs(idx - 1)]
    g.nodes[listener]['state'] = g.nodes[speaker]['state']

    step_count += 1
    if is_homogenous(g) and not tot_steps:
        tot_steps = step_count
        # print('Reached homogeneity in {} steps'.format(tot_steps))

def simulate(upd_rule='normal', num_iter=100):
    if upd_rule == 'reverse':
        upd = update_reverse
    elif upd_rule == 'edge-based':
        upd = update_edge_based
    else:
        upd = update

    num_steps = []
    for _ in range(num_iter):
        initialize()
        while not is_homogenous(g):
            upd()
        num_steps.append(tot_steps)
    print("Average number of steps for consensus in {} rule is:".format(upd_rule), np.mean(num_steps))

simulate('normal')
simulate('reverse')
simulate('edge-based')

# import pycxsimulator
# pycxsimulator.GUI().start(func=[initialize, observe, update])