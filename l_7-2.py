# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:42:42 2022

@author: dvory
"""
a=[]
x=int(input("Введите целое число"))
for i in range (1,x):
    if x%i==0:
        a.append(i)
print (a)
