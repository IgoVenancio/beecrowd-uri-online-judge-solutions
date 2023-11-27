# -*- coding: utf-8 -*-

soma = 0
count_par = 0
while True:
    entrada = int(input())
    if entrada == 0:
        break
    while True:
        if count_par == 5:
            break
        if entrada % 2 == 0:
            soma += entrada
            count_par += 1
        entrada += 1
    print(soma)
    soma = 0
    count_par = 0
