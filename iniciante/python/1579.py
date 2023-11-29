# -*- coding: utf-8 -*-

ho = 'Ho'
exclamacao = '!'

entrada = int(input())
for i in range(entrada):
    if i == entrada - 1:
        print(ho, end='')
    else:
        print(ho, end=' ')
print(exclamacao)
