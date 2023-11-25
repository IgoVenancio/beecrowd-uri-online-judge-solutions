# -*- coding: utf-8 -*-

count = 0
count_positivos = 0
entrada = []
soma = 0
media = 0.0

while count < 6:
    entrada.append(input())
    if '.' in entrada[count]:
        entrada[count] = float(entrada[count])
        if entrada[count] > 0:
            count_positivos += 1
            soma += entrada[count]
    else:
        entrada[count] = int(entrada[count])
        if entrada[count] > 0:
            count_positivos += 1
            soma += entrada[count]
    count += 1

media = soma/count_positivos

print(f'{count_positivos} valores positivos')
print(f'{media:.1f}')
