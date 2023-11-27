# -*- coding: utf-8 -*-

entrada = int(input())

for x in range(1, ((entrada * 4) + 1)):
    if x % 4 == 0:
        print('PUM')
    else:
        print(x, end=' ')
