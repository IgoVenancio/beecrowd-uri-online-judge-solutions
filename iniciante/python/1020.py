# -*- coding: utf-8 -*-

entrada = int(input())

ano = 0
mes = 0
dia = 0
contador = 0

while contador < entrada:
    contador += 1
    if contador == 30:
        mes += 1
        entrada -= contador
        contador = 0
    if mes == 12:
        ano += 1
        entrada -= 5 # ajuste para o ano 365 dias
        mes = 0

dia = contador

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
