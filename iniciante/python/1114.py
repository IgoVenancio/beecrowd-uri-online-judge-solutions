# -*- coding: utf-8 -*-

senha_correta = 2002

while True:
    entrada = int(input())
    if entrada == senha_correta:
        break
    print('Senha Invalida')

print('Acesso Permitido')
