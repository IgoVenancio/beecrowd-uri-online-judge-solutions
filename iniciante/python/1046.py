# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada = [int(x) for x in entrada]

def calculo_hora(a, b):
    count_hora = 0
    while True:
        a +=1
        count_hora +=1
        if a == 24:
            a = 0
        if a == b:
            break
    return count_hora

if entrada[0] == entrada[1]:
    print('O JOGO DUROU 24 HORA(S)')
else:
    print(f'O JOGO DUROU {calculo_hora(entrada[0], entrada[1])} HORA(S)')
