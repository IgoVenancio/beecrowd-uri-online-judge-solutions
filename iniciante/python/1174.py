# -*- coding: utf-8 -*-

lista = []
count = 0

while count < 100:
    entrada = input()
    if '.' in entrada:
        entrada = float(entrada)
    else:
        entrada = int(entrada)
    lista.append(entrada)
    
    count += 1

for i in range(len(lista)):
    if lista[i] <= 10:
        print(f'A[{i}] = {lista[i]:.1f}')
