# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada = [int(x) for x  in entrada]

hora_inic, minuto_inic, hora_final, minuto_final = entrada

def calcular_hora(a, b, c, d):
    count_horas = 0
    count_minutos = 0

    while True:
        b += 1
        count_minutos += 1

        if count_minutos == 60:
            count_horas += 1
            count_minutos = 0

        if a == c and b == d:
            break

        if b == 60:
            a += 1

        if a == c and b == d:
            break

        if b == 60:
            b = 0
        
        if a == c and b == d:
            break

        if a == 24:
            a = 0
        
        if a == c and b == d:
            break

    return count_horas, count_minutos


hora, minuto = calcular_hora(hora_inic, minuto_inic, hora_final, minuto_final)
print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
