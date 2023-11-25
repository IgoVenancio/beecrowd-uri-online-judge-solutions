# -*- coding: utf-8 -*-

entrada = int(input())

for i in range(1, (entrada + 1)):
    if i % 2 == 0:
        print(f'{i}^2 = {pow(i, 2)}')
