# -*- coding: utf-8 -*-

while True:
    entrada = input().split(' ')
    if int(entrada[0]) != 0 and int(entrada[1]) != 0:
        if int(entrada[0]) > 0 and int(entrada[1]) > 0:
            print('primeiro')
        elif int(entrada[0]) > 0 and int(entrada[1]) < 0:
            print('quarto')
        elif int(entrada[0]) < 0 and int(entrada[1]) < 0:
            print('terceiro')
        elif int(entrada[0]) < 0 and int(entrada[1]) > 0:
            print('segundo')
    else:
        break
