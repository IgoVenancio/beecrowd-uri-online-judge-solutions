# -*- coding: utf-8 -*-

count_entradas = 0

qtd_entradas = int(input())
numeros = []
entrada_numeros = ''
media_ponderada = 0.0
while count_entradas < qtd_entradas:
    entrada_numeros = input().split(' ')
    entrada_numeros = [float(x) for x in entrada_numeros]
    
    media_ponderada = (entrada_numeros[0] * 2 +
                       entrada_numeros[1] * 3 +
                       entrada_numeros[2] * 5) / 10
    
    print(f'{media_ponderada:.1f}')

    count_entradas += 1
