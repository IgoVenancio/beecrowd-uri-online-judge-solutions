# -*- coding: utf-8 -*-

count_entrada = 0
total_cobaias = 0
coelho = 0
rato = 0
sapo = 0

qtd_entrada = int(input())
while count_entrada < qtd_entrada:
    entrada = input().split(' ')
    total_cobaias += int(entrada[0])
    if entrada[1] == 'R':
        rato += int(entrada[0])
    elif entrada[1] == 'C':
        coelho += int(entrada[0])
    elif entrada[1] == 'S':
        sapo += int(entrada[0])
    count_entrada += 1

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {(100 * coelho/total_cobaias):.2f} %')
print(f'Percentual de ratos: {(100 * rato/total_cobaias):.2f} %')
print(f'Percentual de sapos: {(100 * sapo/total_cobaias):.2f} %')
