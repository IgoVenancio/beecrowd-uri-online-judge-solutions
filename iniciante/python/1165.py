# -*- coding: utf-8 -*-

count_entrada = 0
count_divisores = 0

qtd_entrada = int(input())
while count_entrada < qtd_entrada:
    entrada = int(input())
    
    for i in range(1, entrada + 1):
        if entrada % i == 0:
            count_divisores += 1
        if count_divisores > 2:
            break
    if count_divisores > 2:
        print(f'{entrada} nao eh primo')
    else:
        print(f'{entrada} eh primo')

    count_divisores = 0
    count_entrada += 1
