# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:32:30 2022

@author: dvory
"""

def f(n, sum):
    sum = sum + n % 10
    if n // 10:
        f(n // 10, sum)
    else:
        print(sum)


f(361074,0)