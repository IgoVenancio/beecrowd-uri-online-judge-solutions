# -*- coding: utf-8 -*-

count_entrada = 0
lista = ['Thor']

entrada = int(input())
while count_entrada < entrada:
    entrada2 = input().split(' ')
    if entrada2[0] in lista:
        print('Y')
    else:
        print('N')
    count_entrada += 1
