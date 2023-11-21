# -*- coding: utf-8 -*-

entrada = int(input())

horas = 0
minutos = 0
segundos = 0
contador = 0

while contador < entrada:
    contador += 1
    if contador == 60:
        minutos += 1
        entrada -= contador
        contador = 0
    if minutos == 60:
        horas += 1
        minutos = 0

segundos = contador

print(f'{horas}:{minutos}:{segundos}')
