# -*- coding: utf-8 -*-

count_grito = 0
numero = 0
while count_grito < 3:
    entrada = input()
    if entrada == '---':
        numero += 0
    elif entrada == '--*':
        numero += 1
    elif entrada == '-*-':
        numero += 2
    elif entrada == '-**':
        numero += 3
    elif entrada == '*--':
        numero += 4
    elif entrada == '*-*':
        numero += 5
    elif entrada == '**-':
        numero += 6
    elif entrada == '***':
        numero += 7
    elif entrada == 'caw caw':
        print(numero)
        numero = 0
        count_grito += 1
