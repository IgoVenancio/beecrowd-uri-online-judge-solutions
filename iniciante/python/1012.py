# -*- coding: utf-8 -*-

entrada = input().split(' ')

area_triangulo = (float(entrada[0]) * float(entrada[2])) / 2
area_circulo = 3.14159 * pow(float(entrada[2]), 2)
area_trapezio = ((float(entrada[0]) + float(entrada[1])) * float(entrada[2])) / 2
area_quadrado = pow(float(entrada[1]), 2)
area_retangulo = (float(entrada[0]) * float(entrada[1]))

print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
