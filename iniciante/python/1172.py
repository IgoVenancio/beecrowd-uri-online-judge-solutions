# -*- coding: utf-8 -*-

lista = []
count_entrada = 0
entrada = 0

while count_entrada < 10:
    entrada = int(input())
    if entrada == 0 or entrada < 0:
        entrada = 1
    lista.append(entrada)
    count_entrada += 1

for i in range(len(lista)):
    print(f'X[{i}] = {lista[i]}')
