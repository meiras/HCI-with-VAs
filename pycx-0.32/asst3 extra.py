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
    global time, config, nextConfig, x, y, state, ant_orientation,ant1_orientation, ant2_orientation, x1, y1, x2, y2

    time = 0
    
    config = SP.zeros([height, width])
 #   config = SP.ones([height, width])


    nextConfig = SP.zeros([height, width])
 #   nextConfig = SP.ones([height, width])
    
    x = 50 #ant col
    y = 50 #ant row
    
    x1 = 25
    y1 = 25
    
    x2 = 75
    y2 = 75
    
    ant_orientation = 'north'
    
    ant1_orientation = 'north'
    
    ant2_orientation = 'north'
    
def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))  
    
def step():
    global time, config, x, y, ant_orientation, ant1_orientation, ant2_orientation, next_orient, state,  x1, y1, x2, y2

    time += 1

    state = config[y, x]

    if state == 0:
        config[y,x]= 1
        if ant_orientation == 'east':
             # FIXME location
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
        
            
    elif state == 1:
        config[y,x]= 0
   # if state == 1: #erorr in elif
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
  
#next ant-----------------------------------------
          
    state = config[y1, x1]


    if state == 0:
        config[y1,x1]= 1
        if ant1_orientation == 'east':
             # FIXME location
            y1 += 1
            ant1_orientation = 'south'
           
            
        elif ant1_orientation == 'north':
            x1 += 1
            ant1_orientation = 'east'
            
            
        elif ant1_orientation == 'south':
            x1 -= 1
            ant1_orientation = 'west'
            
            
        elif ant1_orientation == 'west':
            y1 -= 1
            ant1_orientation = 'north'
        
            
    elif state == 1:
        config[y1,x1]= 0
   # if state == 1: #erorr in elif
        if ant1_orientation == 'north':
            x1 -= 1
            ant1_orientation = 'west'
            
        elif ant1_orientation == 'west':
            y1 += 1
            ant1_orientation = 'south'
            
        elif ant1_orientation == 'south':
            x1 += 1
            ant1_orientation = 'east'
            
        elif ant1_orientation == 'east':
            y1 -= 1
            ant1_orientation = 'north'  
            
            
#last ant
    if state == 0:
        config[y2,x2]= 1
        if ant2_orientation == 'east':
             # FIXME location
            y2 += 1
            ant2_orientation = 'south'
           
            
        elif ant2_orientation == 'north':
            x2 += 1
            ant2_orientation = 'east'
            
            
        elif ant2_orientation == 'south':
            x2 -= 1
            ant2_orientation = 'west'
            
            
        elif ant2_orientation == 'west':
            y2 -= 1
            ant2_orientation = 'north'
        
            
    elif state == 1:
        config[y2,x2]= 0
   # if state == 1: #erorr in elif
        if ant2_orientation == 'north':
            x2 -= 1
            ant2_orientation = 'west'
            
        elif ant2_orientation == 'west':
            y2 += 1
            ant2_orientation = 'south'
            
        elif ant2_orientation == 'south':
            x2 += 1
            ant2_orientation = 'east'
            
        elif ant2_orientation == 'east':
            y2 -= 1
            ant2_orientation = 'north'              
 #   ant_orientation = next_orient
 #   ant_orientation, next_orient = next_orient, ant_orientation
   # config, nextConfig = nextConfig, config
    
#    return ant_col, ant_row, ant_orientation
 
        

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
