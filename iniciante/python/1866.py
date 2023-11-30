# -*- coding: utf-8 -*-

entradas = int(input())
while entradas > 0:
    entrada = int(input())
    if entrada % 2 == 0:
        print(0)
    else:
        print(1)
    entradas -= 1
