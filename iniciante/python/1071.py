# -*- coding: utf-8 -*-

count = 0
lista = []
soma_impar = 0

while count < 2:
    lista.append(int(input()))
    count += 1
lista.sort()

for x in range(lista[0] + 1, lista[1]):
    if x % 2 != 0:
        soma_impar += x

print(soma_impar)
