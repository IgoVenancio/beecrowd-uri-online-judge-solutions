# -*- coding: utf-8 -*-

entrada = float(input())

imposto = 0.0

if entrada >= 0.0 and entrada <= 2000.00:
    print('Isento')
elif entrada >= 2000.01 and entrada <= 3000.00:
    imposto = (entrada - 2000.00) * 0.08
    print(f'R$ {imposto:.2f}')
elif entrada >= 3000.01 and entrada <= 4500.00:
    imposto = 1000.00 * 0.08 + (entrada - 3000.00) * 0.18
    print(f'R$ {imposto:.2f}')
elif entrada > 4500.00:
    imposto = 1000.00 * 0.08 + 1500.00 * 0.18 + (entrada - 4500.00) * 0.28
    print(f'R$ {imposto:.2f}')
