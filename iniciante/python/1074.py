# -*- coding: utf-8 -*-

count_entrada = 0

qtd_entrada = int(input())
while count_entrada < qtd_entrada:
    entrada = int(input())
    if entrada == 0:
        print('NULL')
    else:
        if entrada % 2 == 0:
            if entrada < 0:
                print('EVEN NEGATIVE')
            else:
                print('EVEN POSITIVE')
        else:
            if entrada < 0:
                print('ODD NEGATIVE')
            else:
                print('ODD POSITIVE')

    count_entrada += 1
