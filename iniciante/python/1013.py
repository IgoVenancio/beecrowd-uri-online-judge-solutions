# -*- coding: utf-8 -*-

def maior_tres_numeros(a, b, c):
    maior_ab = (a + b + abs(a - b))/2
    return int((maior_ab + c + abs(maior_ab - c))/2)

entrada = input().split(' ')

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

print(maior_tres_numeros(a, b, c), 'eh o maior')
