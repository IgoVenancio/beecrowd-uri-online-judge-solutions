# -*- coding: utf-8 -*-

entrada = int(input())

while entrada > 0:
    entrada2 = int(input())
    resultado = 2015 - entrada2
    if resultado <= 0:
        print(f'{abs(resultado) + 1} A.C.')
    else:
        print(f'{abs(resultado)} D.C.')
    entrada -= 1
