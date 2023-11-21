# -*- coding: utf-8 -*-

entrada1 = input()
entrada2 = input()

lista_entrada1 = entrada1.split(' ')
lista_entrada2 = entrada2.split(' ')

valor_pagar = int(lista_entrada1[1]) * float(lista_entrada1[2]) + \
              int(lista_entrada2[1]) * float(lista_entrada2[2])

print(f'VALOR A PAGAR: R$ {valor_pagar:.2f}')
