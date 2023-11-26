# -*- coding: utf-8 -*-

entrada = int(input())
count_entrada = 0

while count_entrada < entrada:
    pares = input().split(' ')
    pares = [int(x) for x in pares]

    if pares[1] == 0:
        print('divisao impossivel')
    else:
        print(f'{(pares[0]/pares[1]):.1f}')

    count_entrada += 1
