# -*- coding: utf-8 -*-

def matriz_quadrada(dimensao):
    return [[0 for _ in range(dimensao)] for _ in range(dimensao)]


def area_superior(matriz, limite):
    inicio = 0
    fim = limite
    incremento = 0
    for i in range(limite):
        incremento = 1
        for j in range(inicio, fim):
            matriz[i][j] = incremento
            incremento += 1
        inicio += 1


def area_inferior(matriz, limite):
    linha = 0
    inicio = 0
    fim = limite
    inicio = 0
    fim = limite
    incremento = 0
    for i in range(limite):
        incremento = 1
        for j in range(inicio, fim):
            matriz[j][i] = incremento
            incremento += 1
        inicio += 1


def imprimir_lista(matriz, limite):
    for i in range(limite):
        for j in range(limite):
            if j == entrada - 1:
                print(str(matriz[i][j]).rjust(3))
            else:
                print(str(matriz[i][j]).rjust(3), end=' ')


def imprimir_linha():
    print()


entrada = int(input())
while entrada != 0:
    lista = matriz_quadrada(entrada)
    area_superior(lista, entrada)
    area_inferior(lista, entrada)
    imprimir_lista(lista, entrada)
    imprimir_linha()
    lista.clear()
    entrada = int(input())
