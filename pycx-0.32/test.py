#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:16:47 2018

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

def init():
    global time, config, nextConfig, x, y, state

    time = 0
    
    config = SP.zeros([height, width])
    print config
    for x in xrange(width):
        for y in xrange(height):
     ##       if RD.random() < initProb:
            state = 0

            config[y, x] = state  


    nextConfig = SP.zeros([height, width])
    print nextConfig