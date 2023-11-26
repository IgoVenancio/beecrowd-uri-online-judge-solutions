# -*- coding: utf-8 -*-

entrada = int(input())
count_entrada = 0
soma_impares = 0

while count_entrada < entrada:
    entrada2 = input().split(' ')
    entrada2 = [int(x) for x in entrada2]
    entrada2.sort()
    for x in range(entrada2[0] + 1, entrada2[1]):
        if x % 2 != 0:
            soma_impares += x
    print(soma_impares)
    soma_impares = 0      
    count_entrada += 1
