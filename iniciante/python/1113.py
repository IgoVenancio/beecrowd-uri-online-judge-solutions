# -*- coding: utf-8 -*-

while True:
    entrada = input().split(' ')
    if entrada[0] == entrada[1]:
        break
    if int(entrada[0]) > int(entrada[1]):
        print('Decrescente')
    if int(entrada[0]) < int(entrada[1]):
        print('Crescente')
