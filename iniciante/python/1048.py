# -*- coding: utf-8 -*-

entrada = float(input())

novo_salario = 0.0
reajuste = 0.0
percentual = 0

if entrada >= 0 and entrada <= 400.00:
    novo_salario = entrada + entrada * 0.15
    reajuste = entrada * 0.15
    percentual = 15
elif entrada >= 400.01 and entrada <= 800.00:
    novo_salario = entrada + entrada * 0.15
    reajuste = entrada * 0.12
    percentual = 12
elif entrada >= 800.01 and entrada <= 1200.00:
    novo_salario = entrada + entrada * 0.10
    reajuste = entrada * 0.10
    percentual = 10
elif entrada >= 1200.01 and entrada <= 2000.00:
    novo_salario = entrada + entrada * 0.07
    reajuste = entrada * 0.07
    percentual = 7
else:
    novo_salario = entrada + entrada * 0.04
    reajuste = entrada * 0.04
    percentual = 4

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')
