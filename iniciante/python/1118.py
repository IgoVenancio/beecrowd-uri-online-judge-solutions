# -*- coding: utf-8 -*-

count_notas_validas = 0
soma_notas = 0
novo_calculo = 0
flag_novo_calculo = False

while True:
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
    
    if count_notas_validas == 2:
        print(f'media = {(soma_notas / count_notas_validas):.2f}')
    
        while True:
            flag_novo_calculo = True
            print('novo calculo (1-sim 2-nao)')
            novo_calculo = int(input())
            if novo_calculo == 1 or novo_calculo == 2:
                break
    if novo_calculo == 1 and flag_novo_calculo:
        flag_novo_calculo = False
        soma_notas = 0
        count_notas_validas = 0
        novo_calculo = 0
    elif novo_calculo == 2:
        break
