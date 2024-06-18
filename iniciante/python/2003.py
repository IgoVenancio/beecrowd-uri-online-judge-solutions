# -*- coding: utf-8 -*-

HORAS_MINUTOS = 480

while True:
    try:
        horas_minutos = 0
        entrada = input().split(':')
        horas_minutos = int(entrada[0]) * 60 + int(entrada[1]) + 60
        print('Atraso maximo: ' + str(0) if horas_minutos <= HORAS_MINUTOS 
              else 'Atraso maximo: ' + str(horas_minutos - HORAS_MINUTOS))
    except EOFError:
        break
