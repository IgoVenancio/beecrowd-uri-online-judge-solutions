# -*- coding: utf-8 -*-

while True:
    soma = 0
    entrada = input().split(' ')
    if int(entrada[0]) > 0 and int(entrada[1]) > 0:
        entrada = [int(x) for x in entrada]
        entrada.sort()
        for x in range(entrada[0], entrada[1] + 1):
            soma += x
            print(x, end=' ')
    else:
        break
    print(f'Sum={soma}')
