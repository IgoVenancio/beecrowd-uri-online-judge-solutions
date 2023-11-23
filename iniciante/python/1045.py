# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada = [float(x) for x in entrada]
entrada.sort(reverse=True)
a, b, c = entrada

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if (a * a) == ((b * b) + (c * c)):
        print('TRIANGULO RETANGULO')
    if (a * a) > ((b * b) + (c * c)):
        print('TRIANGULO OBTUSANGULO')
    if (a * a) < ((b * b) + (c * c)):
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    if (a == b and b != c) or (a == c and c != b) or\
       (b == c and c != a):
        print('TRIANGULO ISOSCELES')
