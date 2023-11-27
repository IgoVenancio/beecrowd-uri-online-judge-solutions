# -*- coding: utf-8 -*-

count_entradas = 0
pop_a = 0
pop_b = 0
taxa_a = 0
taxa_b = 0
count_anos = 0

qtd_entradas = int(input())
while count_entradas < qtd_entradas:
    entrada = input().split(' ')
    pop_a = int(entrada[0])
    pop_b = int(entrada[1])
    taxa_a = float(entrada[2])
    taxa_b = float(entrada[3])
    while pop_a <= pop_b:
        pop_a += (taxa_a/100 * pop_a)
        cast_a = str(pop_a).split('.')
        pop_a = int(cast_a[0])
        pop_b += (taxa_b/100 * pop_b)
        cast_b = str(pop_b).split('.')
        pop_b = int(cast_b[0])
        count_anos += 1
    if count_anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{count_anos} anos.')

    count_anos = 0
    count_entradas += 1
