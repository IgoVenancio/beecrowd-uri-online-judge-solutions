# -*- coding: utf-8 -*-

count = 0
count_pares = 0
numeros = []

while count < 6:
    numeros.append(input())
    if '.' in numeros[count]:
        numeros[count] = float(numeros[count])
    else:
        numeros[count] = int(numeros[count])
    if numeros[count] > 0:
        count_pares += 1
    count += 1

print(f'{count_pares} valores positivos')
