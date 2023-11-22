# -*- coding: utf-8 -*-

entrada = input().split(' ')
lista_preco = [4.00, 4.50, 5.00, 2.00, 1.50]
total = lista_preco[int(entrada[0]) - 1] * int(entrada[1])
print(f'Total: R$ {total:.2f}')
