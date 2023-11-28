# -*- coding: utf-8 -*-

linha = int(input())
operacao = input()
soma = 0
# lista = [[] for _ in range(12)]
lista = []

for i in range(12):
    lista.append([])
    for j in range(12):
        entrada = input()
        if '.' in entrada:
            entrada = float(entrada)
        else:
            entrada = int(entrada)
        lista[i].append(entrada)


for i in range(12):
    soma += lista[linha][i]

if operacao == 'S':
    print(soma)
else:
    print(f'{(soma/12):.1f}')
