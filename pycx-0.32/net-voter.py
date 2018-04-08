# Simple Network Dynamics simulator in Python
#
# *** The Voter Model of Opinion Formation on a Network ***
#
# Copyright 2010-2013 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import networkx as NX
import random as RD
import pylab as PL


n = 100 #nodes
p = 0.1 #proablity of edge existing between two nodes. different from speicifc nodes and edges type of renyi
k = 4 # possible states are 4  

def init():
    global g, positions

    g = NX.erdos_renyi_graph(n, p)  #each node, randomly choose state to be in
    for nd in g.nodes():
        g.node[nd]['state'] = RD.choice(range(k))  # all we use to update state is color
    positions = NX.spring_layout(g)

def draw():
    PL.cla()
    NX.draw(g, with_labels = False, pos = positions,
            node_color = [g.node[n]['state'] for n in g.nodes()],
            vmin = 0, vmax = k - 1, cmap = PL.cm.jet)

def step():
    global g
    listener = RD.choice(list(g.nodes())) #go through list of nodes and pull out one listening
    if list(g.neighbors(listener)) != []: #grab neighbors, radomy choose one as soeaker
        speaker = RD.choice(list((g.neighbors(listener))))
        g.node[listener]['state'] = g.node[speaker]['state'] #makelistener state the same as the speaker. can ramdonly ick edge. not just nodes
    #this is an aycnhronous update bc only do one at a time.
    #stablization we saw int he other one doesnt necessarily happen
import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
