# -*- coding: utf-8 -*-

lista = []
entrada = float(input())

for i in range(0, 100):
    lista.append(entrada)
    entrada /= 2
    print(f'N[{i}] = {lista[i]:.4f}')
