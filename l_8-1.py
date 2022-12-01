# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:51:11 2022

@author: dvory
"""

m=int(input("Введите количество строк"))
n=int(input("Введите количество столбцов"))
a=[]
for i in range(m):
    b=[]
    for j in range(n):
        print ("Введите [',i,', ',j,'] 'элемент")
        b.append(int(input()))
    a.append(b)
print("Исходный массив:")
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(m):
    j=1
    while (j!=n):
       if a[i][j]<a[i][j-1]:
           k=a[i][j]
           a[i][j]=a[i][j-1]
           a[i][j-1]=k
           j=0
       j+=1
print("Результат:")
for i in range(m):
     for j in range(n):
         print(a[i][j], end=' ')
     print()
           