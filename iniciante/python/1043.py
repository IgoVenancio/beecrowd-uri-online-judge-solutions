# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada = [float(x) for x in entrada]
area_trapezio = 0.0
perimetro_triangulo = 0.0
a, b, c = entrada

if (a + b) > c and (a + c) > b and (b + c) > a:
    perimetro_triangulo = a + b + c
    print(f'Perimetro = {perimetro_triangulo:.1f}')
else:
    area_trapezio = ((a + b) * c)/2
    print(f'Area = {area_trapezio:.1f}')
