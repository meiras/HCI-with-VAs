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
    for x in xrange(width):
        for y in xrange(height):
     ##       if RD.random() < initProb:
            state = 0

            config[y, x] = state  


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
 
    #placeholder spot for ant
   # 

  #  ant_position = config([ant_row],[ant_col]) #changed from x and y for ant orientation
  #  ant_position = config[y,x] #error on code above for ant position so reverted
  #  orientation = ['east', 'west', 'north', 'south']
    
    ant_col, ant_row, ant_orientation = ant_coordinates(ant_col, ant_row, ant_orientation)
    
    # connect orientation with ant somehow
    


    
def ant_coordinates(ant_col, ant_row, ant_orientation):
    global config, nextConfig
    state = config[ant_col, ant_row]
    if state == 0:
        if ant_orientation == 'north':
            
            state = 1 # FIXME location
            ant_col += 1
            ant_orientation = 'east'
        if ant_orientation == 'east':
            ant_row -= 1
            state = 1 # FIXME location
            ant_orientation = 'south'
        if ant_orientation == 'south':
            ant_col -= 1
            state = 1 # FIXME location  
            ant_orientation = 'west'
        elif ant_orientation == 'west':
            ant_row += 1
            state = 1 # FIXME location 
            ant_orientation = 'north'
        state = 1
        nextConfig[ant_col, ant_row] = state
    if state == 1: #erorr in elif
        if ant_orientation == 'north':
            
             # FIXME location
            ant_col -= 1
            ant_orientation = 'west'
        if ant_orientation == 'west':
            ant_row -= 1
             # FIXME location
            ant_orientation = 'south'
        if ant_orientation == 'south':
            ant_col += 1
             # FIXME location  
            ant_orientation = 'east'
        elif ant_orientation == 'east':
            ant_row += 1
             # FIXME location 
            ant_orientation = 'north'
        state = 0
    
    config, nextConfig = nextConfig, config
    return ant_row, ant_col, ant_orientation
 #   def leftrotate():
 #       numpy.rot90
 #       numpy.rot90
 #       numpy.rot90
        
  #  degree+90 = 90
    
    # if state == 0:
        
     #   config
        
      #  numpy.rot90
    #    state = 1 ## swap and assign to one that was before -1
    #    dx = dx + 1
        
        
        
   # else: 
   #     dx += 1
    #    state = 0
        
        
 #   turn 90, flip color, move forward
  
###  nextConfig[y, x] = state
     
           

     #       for dx in xrange(-1, 2):
     #           for dy in xrange(-1, 2):
     #               numberOfAlive += config[(y+dy)%height, (x+dx)%width]
     

    

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])