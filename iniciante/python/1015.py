# -*- coding: utf-8 -*-

entrada1 = input().split(' ')
entrada2 = input().split(' ')

x1 = float(entrada1[0]) 
x2 = float(entrada2[0]) 
y1 = float(entrada1[1]) 
y2 = float(entrada2[1]) 

distancia_pontos = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

print(f'{distancia_pontos:.4f}')
