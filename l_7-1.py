# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:56:39 2022

@author: dvory
"""
def NOD (a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
A=int(input("Введите значение A"))
B=int(input("Введите значение B"))
C=int(input("Введите значение C"))
D=int(input("Введите значение D"))
if (A * D - B * C) > 0:
    chisl = A * D - B * C
    znam = B * D
    n=(NOD(chisl,znam))
    print(f'{chisl // n}/{znam // n}')
else:
    chisl = B * C - A * D
    znam = B * D
    n=(NOD(chisl,znam))
    print("-",f'{chisl // n}/{znam // n}')