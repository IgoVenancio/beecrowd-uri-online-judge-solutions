# -*- coding: utf-8 -*-

count = 0
lista_par = []
lista_impar = []

while count < 15:
    entrada = int(input())
    if entrada % 2 == 0:
        lista_par.append(entrada)
    else:
        lista_impar.append(entrada)
    if len(lista_impar) == 5:
        for i in range(len(lista_impar)):
            print(f'impar[{i}] = {lista_impar[i]}')
        lista_impar.clear()
    if len(lista_par) == 5:
        for i in range(len(lista_par)):
            print(f'par[{i}] = {lista_par[i]}')
        lista_par.clear()

    count += 1


for i in range(len(lista_impar)):
    print(f'impar[{i}] = {lista_impar[i]}')
lista_impar.clear()

for i in range(len(lista_par)):
    print(f'par[{i}] = {lista_par[i]}')
lista_par.clear()
