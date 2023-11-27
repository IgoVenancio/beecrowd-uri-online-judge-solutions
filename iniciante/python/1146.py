# -*- coding: utf-8 -*-

while True:
    entrada = int(input())
    if entrada == 0:
        break
    for x in range(1, entrada + 1):
        if x == entrada:
            print(x)
        else:
            print(x, end=' ')
