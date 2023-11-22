# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada = [int(x) for x in entrada]

if entrada[0] % entrada[1] == 0 or \
   entrada[1] % entrada[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
