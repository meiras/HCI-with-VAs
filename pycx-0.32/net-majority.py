# Simple Network Dynamics simulator in Python
#
# *** Majority Rule on a Social Network ***
#
# Copyright 2011-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import networkx as NX
import random as RD

RD.seed()

col = {0:'w', 1:'k'}

def init():
    global time, network, nextNetwork, positions

    time = 0
    
    network = NX.random_regular_graph(4, 100) #rgegualr random graph
    for n in network.nodes():
        network.node[n]['state'] = RD.choice([0, 1]) #state is binary

    nextNetwork = network.copy()

    positions = NX.spring_layout(network)

def draw():
    PL.cla()
    NX.draw(network, pos = positions, node_color = [col[network.node[n]['state']] for n in network.nodes()])
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, network, nextNetwork

    time += 1

    for n in network.nodes():
        total = network.node[n]['state']
        nbs = list(network.neighbors(n))  #added list() here.  ask to find neighbors o fgiven node. force it into list
        for nb in nbs: #count all neighbors and state
            total += network.node[nb]['state']
        if total * 2 > len(nbs) + 1:
            nextNetwork.node[n]['state'] = 1 #if majority of my neigbors are state 1, set me to state 1
        elif total * 2 < len(nbs) + 1:
            nextNetwork.node[n]['state'] = 0
        else:
            nextNetwork.node[n]['state'] = network.node[n]['state']
            #randomyl initiatilize, then let assign rule based on neighbors, then self sorting

    network, nextNetwork = nextNetwork, network

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
