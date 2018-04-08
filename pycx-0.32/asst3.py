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
import numpy as np #this might be useful for moving right and left numpy.rot90


RD.seed()

width = 50
height = 50
initProb = 0.0004

def init():
    global time, config, nextConfig, x, y

    time = 0
    
    config = SP.zeros([height, width])
    for x in xrange(width):
        for y in xrange(height):
     ##       if RD.random() < initProb:
            state = 0

            config[y, x] = state  
         #   state = 0
         #   config[y, x] = state

    nextConfig = SP.zeros([height, width])
    
def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))
    
    
    
def step():
    global time, config, nextConfig

    time += 1
    
    #placeholder spot for ant
    dx = 5
    dy = 5 
    state = config[y, x]
    numberOfAlive = 0
    
 #   def leftrotate():
 #       numpy.rot90
 #       numpy.rot90
 #       numpy.rot90
        
  #  degree+90 = 90
    
    if state == 0:
        
        config
        
        numpy.rot90
        state = 1 ## swap and assign to one that was before -1
        dx = dx + 1
        
        
        
    else: 
        dx += 1
        state = 0
        
        
 #   turn 90, flip color, move forward
    nextConfig[y, x] = state
     
           

     #       for dx in xrange(-1, 2):
     #           for dy in xrange(-1, 2):
     #               numberOfAlive += config[(y+dy)%height, (x+dx)%width]
     

    config, nextConfig = nextConfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
