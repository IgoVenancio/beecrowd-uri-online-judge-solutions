# -*- coding: utf-8 -*-

entrada = input().split()
abas_abertas = int(entrada[0])
acoes = int(entrada[1])
while acoes > 0:
    acao = input()
    abas_abertas += (1, -1)[acao == 'clicou']
    acoes -= 1
print(abas_abertas)
