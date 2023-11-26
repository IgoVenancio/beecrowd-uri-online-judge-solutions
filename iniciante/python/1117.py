# -*- coding: utf-8 -*-

count_notas_validas = 0
soma_notas = 0

while count_notas_validas < 2:
    entrada = input()
    if '.' in entrada:
        entrada = float(entrada)
    else:
        entrada = int(entrada)

    if entrada >= 0 and entrada <= 10:
        soma_notas += entrada
        count_notas_validas += 1
    else:
        print('nota invalida')

print(f'media = {(soma_notas / count_notas_validas):.2f}')
