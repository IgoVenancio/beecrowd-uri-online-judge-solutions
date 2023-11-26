# -*- coding: utf-8 -*-

count = 0
entrada = []
while count < 2:
    entrada.append(int(input()))
    count += 1

entrada.sort()

for numero in range(entrada[0] + 1, entrada[1]):
    if numero % 5 == 2 or numero % 5 == 3:
        print(numero)
