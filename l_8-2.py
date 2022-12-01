# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:26:52 2022

@author: dvory
"""

m=int(input("Введите количество строк"))
n=int(input("Введите количество столбцов"))
a=[]
print ("Введите элементы матрицы без повторений")
for i in range(m):
    b=[]
    for j in range(n):
        b.append(int(input()))
    a.append(b)
print("Исходный массив:")
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(m):
    k=0
    for j in range(n):
        if a[i][j]<a[i][k]:
            k=j
    if a[i][k]%2==0:
        a[i][k]=0
    else:
        a[i][k]=1
print("Результат:")
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()