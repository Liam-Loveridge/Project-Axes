"""
    Fluffy Computing Machine: Day 13
    I-V Characteristic 
    Liam Loveridge | May 2020
"""

#TODO: Clean up code and make it more presentable

#Dependencies 
from pylab import *

#Data - from a textbook
current = array([-1.65,-1.63,-1.52,-1.34,-1.14,-0.82,0.00,0.81,1.12,1.36,1.53,1.62,1.64])
pd = array([-9.0,-7.5,-6.0,-4.5,-3.0,-1.5,0.0,1.5,3.0,4.5,6.0,7.5,9.0])

#Graphing 
plot(pd, current, 'kx')

#Formatting 
title("I-V Characteristic")
xlabel("Potential Difference /V")
ylabel("Current /A")

#Saving
savefig('Fig.png')