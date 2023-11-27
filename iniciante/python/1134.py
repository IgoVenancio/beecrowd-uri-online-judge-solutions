# -*- coding: utf-8 -*-

alcool = 0
gasolina = 0
diesel = 0

while True:
    entrada = int(input())
    if entrada == 4:
        break
    if entrada == 1:
        alcool += 1
    elif entrada == 2:
        gasolina += 1
    elif entrada == 3:
        diesel += 1

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
