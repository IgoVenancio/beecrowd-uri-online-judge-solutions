# -*- coding: utf-8 -*-

PI = 3.14
while True:
    try:
        volume = float(input())
        diametro = float(input())
        altura = volume / (PI * (diametro / 2)**2)
        area = PI * (diametro/2) * (diametro/2)
        print(f'ALTURA = {altura:.2f}')
        print(f'AREA = {area:.2f}')

    except EOFError:
        break
