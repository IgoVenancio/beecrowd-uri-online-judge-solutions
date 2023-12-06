# -*- coding: utf-8 -*-

entrada = input().split()

porcentagem = ((float(entrada[1]) - float(entrada[0])) /
               float(entrada[0])) * 100

print(f'{porcentagem:.2f}%')
