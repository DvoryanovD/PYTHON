# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:51:12 2022

@author: dvory
"""

a=[]
b=[]
n=0
k=0
for i in range (10):
    print("Введите ", i, "элемент:")
    a.append(int(input()))
print ("Исходный массив:", a)
for i in range(10):
    for j in range (i+1,10):
        if a[i]==a[j]:
            n+=1
            b.append(a[j])
            break
print (b)
for i in range(n):
    a.remove(b[i])
print ("Результат:", a)            
    
    