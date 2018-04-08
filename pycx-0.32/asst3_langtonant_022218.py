#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 14:08:11 2018

@author: meira
"""

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP


RD.seed()

width = 100
height = 100


#might help with orientation to define

def init():
    global time, config, nextConfig, x, y, state, ant_orientation 

    time = 0
    
    config = SP.zeros([height, width])

    nextConfig = SP.zeros([height, width])
    
    #initial placement and orientation of ant
    x = 50 #ant col
    y = 50 #ant row
    ant_orientation = 'north'
    
def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))  
    
def step():
    global time, config, x, y, ant_orientation, next_orient, state

    time += 1

    state = config[y, x]

#if state is 0, make it 1, then orient 90 degrees to right and go forward
    if state == 0:
        config[y,x]= 1
        if ant_orientation == 'east':
            y += 1
            ant_orientation = 'south'
           
            
        elif ant_orientation == 'north':
            x += 1
            ant_orientation = 'east'
            
            
        elif ant_orientation == 'south':
            x -= 1
            ant_orientation = 'west'
            
            
        elif ant_orientation == 'west':
            y -= 1
            ant_orientation = 'north'
        
    # if state is 1, make it 0, then orient 90 degrees to left and go forward        
    elif state == 1:
        config[y,x]= 0

        if ant_orientation == 'north':
            x -= 1
            ant_orientation = 'west'
            
        elif ant_orientation == 'west':
            y += 1
            ant_orientation = 'south'
            
        elif ant_orientation == 'south':
            x += 1
            ant_orientation = 'east'
            
        elif ant_orientation == 'east':
            y -= 1
            ant_orientation = 'north'
            
    
        

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
