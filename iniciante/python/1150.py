# -*- coding: utf-8 -*-

soma = 0
z = 0
count_numeros = 0
x = int(input())
while True:
    z = int(input())
    if z > x:
        break

for i in range(x, z):
    soma += i
    count_numeros += 1
    if soma > z:
        break
print(count_numeros)
