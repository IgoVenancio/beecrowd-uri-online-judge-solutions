# -*- coding: utf-8 -*-

tabela = {
    '1001': 1.5,
    '1002': 2.5,
    '1003': 3.5,
    '1004': 4.5,
    '1005': 5.5
}

qtd_entrada = int(input())
saida = 0
for _ in range(qtd_entrada):
    entrada = input().split()
    saida += tabela[entrada[0]] * int(entrada[1])
print(f'{saida:.2f}')
