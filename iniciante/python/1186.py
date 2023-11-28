# -*- coding: utf-8 -*-

operacao = input()
soma = 0
lista = []
linha = 1
final = 12
count_numeros = 0
inicio = 11

for i in range(12):
    lista.append([])
    for j in range(12):
        entrada = input()
        if '.' in entrada:
            entrada = float(entrada)
        else:
            entrada = int(entrada)
        lista[i].append(entrada)

for j in range(11):
    for i in range(inicio, final):
        soma += lista[linha][i]
        count_numeros += 1
    inicio -= 1
    linha += 1

if operacao == 'S':
    print(soma)
else:
    print(f'{(soma/count_numeros):.1f}')
