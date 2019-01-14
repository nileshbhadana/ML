#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:33:39 2019

@author: nilesh
"""
import time
import psutil,matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y = [], []
while True:
    x.append(i)
    y.append(psutil.cpu_percent())
    print(len(y))
    if len(y) >=20:
        y.pop(0)
        x.pop(0)
    ax.plot(x, y, color='b')  
    fig.canvas.draw()
    
    ax.set_xlim(left=max(0, i-30), right=i+30)
    
    time.sleep(0.1)
    i += 1