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
#initProb = 0.0004

#might help with orientation to define

def init():
    global time, config, nextConfig, x, y, state, ant_orientation 

    time = 0
    
    config = SP.zeros([height, width])
 #   config = SP.ones([height, width])


    nextConfig = SP.zeros([height, width])
 #   nextConfig = SP.ones([height, width])
    
    x = 25 #ant col
    y = 25 #ant row
  
    
 #   state = config[y, x]
 
 

    ant_orientation = 'north'
    
def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))
    
    
    
def step():
    global time, config, nextConfig, x, y, ant_orientation, next_orient

    time += 1
   # print ant_row, ant_col, ant_orientation 


    state = config.item((y, x))

    if state == 1: #erorr in elif
        if ant_orientation == 'north':
           # state = 0 # FIXME location
            x -= 1
            next_orient = 'west'
            nextConfig[y, x] = 0
        elif ant_orientation == 'west':
         #   state = 0
            y += 1
            next_orient = 'south'
            nextConfig[y, x] = 0
            
        elif ant_orientation == 'south':
          #  state = 0
            x += 1
            next_orient = 'east'
            nextConfig[y, x] = 0
            
        elif ant_orientation == 'east':
          #  state = 0
            y -= 1
            next_orient = 'north'
            nextConfig[y, x] = 0

    elif state == 0:
        if ant_orientation == 'east':
           # state = 1 # FIXME location
            y += 1
            next_orient = 'south'
            nextConfig[y, x] = 1
            
        elif ant_orientation == 'north':
           
            x += 1
            next_orient = 'east'
            nextConfig[y, x] = 1
            
        elif ant_orientation == 'south':
            #state = 1 # FIXME location  
            x -= 1
            next_orient = 'west'
            nextConfig[y, x] = 1
            
        elif ant_orientation == 'west':
          #  state = 1 # FIXME location 
            y -= 1
            next_orient = 'north'
            nextConfig[y, x] = 1
    

    ant_orientation = next_orient
    config, nextConfig = nextConfig, config
    
#    return ant_col, ant_row, ant_orientation
 
        

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
