# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada = [int(x) for x in entrada]
lista_ordenada = sorted(entrada)

for numero in lista_ordenada:
    print(numero)
print()
for numero in entrada:
    print(numero)
