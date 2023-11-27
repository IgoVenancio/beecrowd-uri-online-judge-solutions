# -*- coding: utf-8 -*-

entrada = int(input())
count_entrada = 0
soma = 0
while count_entrada < entrada:
    entrada2 = input().split(' ')
    entrada2 = [int(x) for x in entrada2]
    while True:
        if entrada2[1] == 0:
            break
        if entrada2[0] % 2 != 0:
            soma += entrada2[0]
            entrada2[1] -= 1
        entrada2[0] += 1
    print(soma)
    soma = 0
    count_entrada += 1
