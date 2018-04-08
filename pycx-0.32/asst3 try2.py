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
ant = 1

def init():
    global time, config, nextConfig, x, y

    time = 0
    
    config = SP.zeros([height, width])
    for x in xrange(width):
        for y in xrange(height):
     ##       if RD.random() < initProb:
            state = 0

            config[y, x] = state  


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
   # 
    ant_row = 25
    ant_col = 25
    ant_position = config([ant_row],[ant_col]) #changed from x and y for ant orientation
   # orientation = config([ant_row],[ant_col+1])
    orientation = ['east', 'west', 'north', 'south']
  #  ant_position = ((height*width)/2) + int(width/2))

#define orientation

    
    def ant_coordinates(ant_row, ant_col, orientation):
        state = config[ant_row][ant_col]
        if state == 0:
            if orientation == 'east':
                
                state = 1
                ant_row += 1
            elif orientation == 'south':
                ant_col -= 1
                state = 1
        #state = 1
        return ant_row, ant_col, orientation
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
    nextConfig[y, x] = state
     
           

     #       for dx in xrange(-1, 2):
     #           for dy in xrange(-1, 2):
     #               numberOfAlive += config[(y+dy)%height, (x+dx)%width]
     

    config, nextConfig = nextConfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
