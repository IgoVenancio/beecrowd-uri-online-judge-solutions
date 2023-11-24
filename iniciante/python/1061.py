# -*- coding: utf-8 -*-

entrada1 = input()
entrada2 = input()
entrada3 = input()
entrada4 = input()

dia_inicio = entrada1.split(' ')
dia_inicio = int(dia_inicio[1])
dia_final = entrada3.split(' ')
dia_final = int(dia_final[1])
hora_inicio = int(entrada2[0:2])
hora_final = int(entrada4[0:2])
minuto_inicio = int(entrada2[5:7])
minuto_final = int(entrada4[5:7])
segundo_inicio = int(entrada2[-2:])
segundo_final = int(entrada4[-2:])

dia = dia_final - dia_inicio
hora = hora_final - hora_inicio
minuto = minuto_final - minuto_inicio
segundo = segundo_final - segundo_inicio

if segundo < 0:
    segundo = 60 + segundo
    minuto -= 1
if minuto < 0:
    minuto = 60 + minuto
    hora -= 1
if hora < 0:
    hora = 24 + hora
    dia -= 1


print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundo} segundo(s)')
