# -*- coding: utf-8 -*-

notas = [100, 50, 20, 10, 5, 2]

while True:
    count_notas = 0

    entrada = input().split()

    numero_1 = int(entrada[0])
    numero_2 = int(entrada[1])

    if numero_1 == numero_2 == 0:
        break

    troco = numero_2 - numero_1

    for x in notas:
        if x <= troco:
            troco -= x
            count_notas += 1
    if count_notas == 2:
        print('possible')
    else:
        print('impossible')
