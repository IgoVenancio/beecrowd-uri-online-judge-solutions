# -*- coding: utf-8 -*-

nome_vendedor = input()
salario_fixo = float(input())
total_vendas_mes = float(input())

total_receber = salario_fixo + 0.15 * total_vendas_mes

print(f'TOTAL = R$ {total_receber:.2f}')
