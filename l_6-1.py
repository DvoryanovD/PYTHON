# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:51:12 2022

@author: dvory
"""

a=[]
n=10
for i in range (n):
    print("Введите ", i, "элемент:")
    a.append(int(input()))
print ("Исходный массив:", a)
for i in range(n-1):
    if a[i]<0 and a[i+1]<0:
        print (a[i], a[i+1])
            
    
    