# -*- coding: utf-8 -*-

lista = []

lista.append(0)
lista.append(1)

entrada = int(input())

for i in range(2, entrada):
    lista.append(lista[i - 1] + lista[i - 2])

for i in range(entrada):
    if i == entrada - 1:
        print(lista[i])
    else:
        print(lista[i], end=' ')
