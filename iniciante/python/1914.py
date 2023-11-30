# -*- coding: utf-8 -*-

entradas = int(input())

while entradas > 0:
    entrada1 = input().split(' ')
    entrada2 = input().split(' ')
    if entrada1[1] == 'PAR' and ((int(entrada2[0]) + int(entrada2[1])) % 2 == 0):
        print(entrada1[0])
    elif entrada1[1] == 'IMPAR' and ((int(entrada2[0]) + int(entrada2[1])) % 2 != 0):
        print(entrada1[0])
    elif entrada1[3] == 'IMPAR' and ((int(entrada2[0]) + int(entrada2[1])) % 2 != 0):
        print(entrada1[2])
    elif entrada1[3] == 'PAR' and ((int(entrada2[0]) + int(entrada2[1])) % 2 == 0):
        print(entrada1[2])

    entrada1.clear()
    entrada2.clear()
    entradas -= 1
