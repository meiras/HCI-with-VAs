# Simple Network Dynamics simulator in Python
#
# *** Network Synchronization in the Kuramoto model ***
#
# Copyright 2010-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import networkx as NX
import random as RD
import math as MT

dt = 0.01
sigma = 10.

def init():
    global time, network, positions, nextNetwork

    time = 0

    network = NX.watts_strogatz_graph(100, 4, 0.2)
    for i in network.nodes():
        network.node[i]['theta'] = RD.uniform(0, 2 * MT.pi)
        network.node[i]['omega'] = RD.gauss(2 * MT.pi, 0.05)

    positions = NX.spring_layout(network)

    nextNetwork = network.copy()

def draw():
    PL.subplot(1, 2, 1)
    PL.cla()
    thetas = [network.node[nd]['theta'] for nd in network.nodes()]
    NX.draw(network, with_labels = False, pos = positions,
            cmap = PL.cm.hsv, vmin = -1, vmax = 1,
            node_color = [MT.sin(th) for th in thetas])
    PL.axis('image')
    PL.title('t = ' + str(time))

    PL.subplot(1, 2, 2)
    PL.cla()
    PL.plot([MT.cos(th) for th in thetas], [MT.sin(th) for th in thetas], 'bo')
    PL.axis('image')
    PL.axis([-1, 1, -1, 1])
    PL.title('Node phases')

def step():
    global time, network, nextNetwork
    
    time += dt

# this is where get phase state of inidivual node (represented as theta). get it to adjust based on formula on 58 to adjust to neighbors
    for nd in network.nodes():
        th = network.node[nd]['theta']
        nbrs = list(network.neighbors(nd))
        nextNetwork.node[nd]['theta'] = th + dt * (
            network.node[nd]['omega'] + #updating thera. turning it into agent level variable rha my agent or node owns. update arrocing to  below sigma
            sigma * sum([MT.sin(network.node[nb]['theta'] - th) for nb in nbrs]) / len(nbrs) # sum of sin of neighbors hteta and my theta...list compherehension where iterates through, and sums them together. plus omega which is naturally sead want to go. so how fast want to go and how uch adjusting to neighrbors
            ) #sigma is the alpha. multiply that by change in time. when take contniuous model in ABM< must discretize it. changes to formula are to adjust it to accommodate step structure.

    network, nextNetwork = nextNetwork, network

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
