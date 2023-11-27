# -*- coding: utf-8 -*-

entrada = int(input())

for i in range(1, entrada + 1):
    if entrada % i == 0:
        print(i)
