# -*- coding: utf-8 -*-

menor = 10000000
posicao = 0
entrada = int(input())
numeros = input().split(' ')

for i in range(entrada):
    if int(numeros[i]) < menor:
        menor = int(numeros[i])
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
