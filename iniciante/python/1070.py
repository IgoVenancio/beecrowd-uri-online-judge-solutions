# -*- coding: utf-8 -*-

entrada = int(input())
count_impar = 0
while count_impar < 6:
    if entrada % 2 != 0:
        print(entrada)
        count_impar += 1
    entrada += 1
 
