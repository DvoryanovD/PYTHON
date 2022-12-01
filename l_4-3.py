# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:11:58 2022

@author: dvory
"""

a=1
s=1
t=0
n=int(input())
while a<=n:
    s=s*a
    a=a+1
    t+=s
print (t)