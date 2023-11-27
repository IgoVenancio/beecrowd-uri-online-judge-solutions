# -*- coding: utf-8 -*-

casos_teste = int(input())
soma_divisores = 0

while casos_teste > 0:
    entrada = int(input())
    for i in range(1, entrada):
        if entrada % i == 0:
            soma_divisores += i
    if soma_divisores == entrada:
        print(f'{entrada} eh perfeito')
    else:
        print(f'{entrada} nao eh perfeito')
    soma_divisores = 0
    casos_teste -= 1
