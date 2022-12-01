# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:42:15 2022

@author: dvory
"""

import math

x=int(input("Значение x = "))
t=int(input("Значение t = "))

z = ((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print ("z = {0:.2f}".format (z))
