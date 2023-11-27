# -*- coding: utf-8 -*-

soma_idades = 0
count_idades = 0
while True:
    entrada = int(input())
    if entrada < 0:
        break
    count_idades += 1
    soma_idades += entrada

print(f'{(soma_idades/count_idades):.2f}')
