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
    global time, config, nextConfig, ant_row, ant_col, state, ant_orientation 

    time = 0
    
    config = SP.zeros([height, width])
 #   for x in xrange(width):
 #       for y in xrange(height):
     ##       if RD.random() < initProb:
 #           state = 0

          #  config[y, x] = state  


    nextConfig = SP.zeros([height, width])
    
    x = 25
    y = 25
  
    
 #   state = config[y, x]
    ant_row = x
    ant_col = y
    ant_orientation = 'north'
    
def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))
    
    
    
def step():
    global time, config, nextConfig, ant_row, ant_col, state, ant_orientation 

    time += 1
   

  #call function, feed in
 #   ant_col, ant_row, ant_orientation = ant_coordinates(ant_col, ant_row, ant_orientation)
    
    # connect orientation with ant somehow
    

    
#def ant_coordinates(ant_col, ant_row, ant_orientation):
 #   global config, nextConfig
    state = config[ant_col, ant_row]
    if state == 0:
        if ant_orientation == 'north':
           
            ant_col += 1
            ant_orientation = 'east'
            nextConfig[ant_col, ant_row] = 1
            
        if ant_orientation == 'east':
           # state = 1 # FIXME location
            ant_row += 1
            ant_orientation = 'south'
            nextConfig[ant_col, ant_row] = 1
            
        if ant_orientation == 'south':
            #state = 1 # FIXME location  
            ant_col -= 1
            ant_orientation = 'west'
            nextConfig[ant_col, ant_row] = 1
            
        elif ant_orientation == 'west':
          #  state = 1 # FIXME location 
            ant_row -= 1
            ant_orientation = 'north'
            nextConfig[ant_col, ant_row] = 1
    
       # nextConfig[ant_col, ant_row] = state 

        ##state = 1
       
    elif state == 1: #erorr in elif
        if ant_orientation == 'north':
           # state = 0 # FIXME location
            ant_col -= 1
            ant_orientation = 'west'
            nextConfig[ant_col, ant_row] = 0
            
        if ant_orientation == 'west':
         #   state = 0
            ant_row += 1
            ant_orientation = 'south'
            nextConfig[ant_col, ant_row] = 0
            
        if ant_orientation == 'south':
          #  state = 0
            ant_col += 1
            ant_orientation = 'east'
            nextConfig[ant_col, ant_row] = 0
            
        elif ant_orientation == 'east':
          #  state = 0
            ant_row -= 1
            ant_orientation = 'north'
            nextConfig[ant_col, ant_row] = 0
            
  #  nextConfig[ant_col, ant_row] = state
    
    config, nextConfig = nextConfig, config
#    return ant_col, ant_row, ant_orientation
 
        

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
