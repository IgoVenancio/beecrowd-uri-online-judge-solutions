# -*- coding: utf-8 -*-

lista = []
count_entrada = 0
troca = 0

while count_entrada < 20:
    entrada = int(input())
    lista.append(entrada)
    count_entrada += 1

for i in range(0, 10):
    troca = lista[i]
    lista[i] = lista[len(lista) - 1 - i]
    lista[len(lista) - 1 - i] = troca

for i in range(0, 20):
    print(f'N[{i}] = {lista[i]}')
