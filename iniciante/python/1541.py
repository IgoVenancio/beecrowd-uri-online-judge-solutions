# -*- coding: utf-8 -*-

while True:
    entrada = input().split(' ')
    if len(entrada) == 1:
        break
    a = int(entrada[0])
    b = int(entrada[1])
    c = int(entrada[2])
    resultado = int(((a * b * 100)/c) ** (1/2))
    print(resultado)
