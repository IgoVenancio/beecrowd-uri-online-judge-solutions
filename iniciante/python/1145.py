# -*- coding: utf-8 -*-

count_numeros = 0

entrada = input().split(' ')
for x in range(1, int(entrada[1]) + 1):
    print(x, end='')
    count_numeros += 1
    if count_numeros == int(entrada[0]):
        print()
        count_numeros = 0
    else:
        print(end=' ')
