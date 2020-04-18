"""
    Hookes.py
    Example code for the whole project
    Written by Liam Loveridge (c) 2020

"""

# TODO: Add regression line to the code
# TODO: Refactor to make it more general

#Dependencies
from pylab import *

#Inputs - Using experimental data for Hooke's Law
mass = array([0,0.1,0.2,0.4,0.5,0.6,0.8], dtype = float) #X
length = array([0.055,0.074,0.089,0.124,0.135,0.181,0.193], dtype = float) #Y

#Graphing
plot(mass, length, 'kx', label ='data')

#Formatting
title("Hooke's Law Example")
xlabel('Mass (kg)')
ylabel('Length (m)')
legend (loc = 'best')

#Output to file
savefig('IO/Output/Hookes.png')
