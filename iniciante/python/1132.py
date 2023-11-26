# -*- coding: utf-8 -*-

count = 0
entrada = []
soma_nao_multiplos = 0
while count < 2:
    entrada.append(int(input()))
    count += 1

entrada.sort()

for numero in range(entrada[0], entrada[1] + 1):
    if numero % 13 == 0:
        continue
    soma_nao_multiplos += numero

print(soma_nao_multiplos)
