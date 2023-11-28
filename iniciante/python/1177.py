# -*- coding: utf-8 -*-

count = 0

entrada = int(input())
for i in range(0, 1000):
    print(f'N[{i}] = {count}')
    count += 1
    if count == entrada:
        count = 0
