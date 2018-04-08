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


    nextConfig = SP.zeros([height, width])
    
    x = 25
    y = 25
  
    
 #   state = config[y, x]
 
 
  #  ant_row = x
  #  ant_col = y
    ant_orientation = 'north'
    
def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))
    
    
    
def step():
    global time, config, nextConfig, ant_row, ant_col, ant_orientation, next_orient

    time += 1
   # print ant_row, ant_col, ant_orientation 


    state = config[ant_row, ant_col]
    if state == 1: #erorr in elif
        if ant_orientation == 'north':
           # state = 0 # FIXME location
            ant_col -= 1
            ant_row = ant_row
            next_orient = 'west'
            nextConfig[ant_row, ant_col] = 0
            
        elif ant_orientation == 'west':
         #   state = 0
            ant_row += 1
            next_orient = 'south'
            nextConfig[ant_row, ant_col] = 0
            
        elif ant_orientation == 'south':
          #  state = 0
            ant_col += 1
            next_orient = 'east'
            nextConfig[ant_row, ant_col] = 0
            
        elif ant_orientation == 'east':
          #  state = 0
            ant_row -= 1
            next_orient = 'north'
            nextConfig[ant_row, ant_col] = 0
    elif state == 0:
        if ant_orientation == 'east':
           # state = 1 # FIXME location
            ant_row += 1
            ant_col = ant_col
            next_orient = 'south'
            nextConfig[ant_row, ant_col] = 1
            
        elif ant_orientation == 'north':
           
            ant_col += 1
            next_orient = 'east'
            nextConfig[ant_row, ant_col] = 1
            
        
            
        elif ant_orientation == 'south':
            #state = 1 # FIXME location  
            ant_col -= 1
            next_orient = 'west'
            nextConfig[ant_row, ant_col] = 1
            
        elif ant_orientation == 'west':
          #  state = 1 # FIXME location 
            ant_row -= 1
            next_orient = 'north'
            nextConfig[ant_row, ant_col] = 1
    

    ant_orientation = next_orient
    config, nextConfig = nextConfig, config
    
#    return ant_col, ant_row, ant_orientation
 
        

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
