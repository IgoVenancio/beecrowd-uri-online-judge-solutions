# -*- coding: utf-8 -*-

lista_fibo = []
lista_fibo.append(0)
lista_fibo.append(1)
for i in range(2, 61):
    lista_fibo.append(lista_fibo[i - 1] + lista_fibo[i - 2])

entrada = int(input())
while entrada > 0:
    caso = int(input())
    print(f'Fib({caso}) = {lista_fibo[caso]}')
    entrada -= 1
