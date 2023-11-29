# -*- coding: utf-8 -*-

def matriz_quadrada(dimensao, default=0):
    return [[default for _ in range(dimensao)] for _ in range(dimensao)]


def preencher_matriz(matriz, dimensao):
    incremento = 0
    incremento2 = 1
    for i in range(dimensao):
        incremento = incremento2
        for j in range(dimensao):
            matriz[i][j] = incremento
            incremento *= 2
        incremento2 *= 2


def maior_matriz(matriz, dimensao):
    return matriz[dimensao - 1][dimensao - 1]


def imprimir_linha():
    print()


def imprimir_matriz(matriz, dimensao):
    maior = maior_matriz(matriz, dimensao)
    for i in range(dimensao):
        for j in range(dimensao):
            if j == dimensao - 1:
                print(str(matriz[i][j]).rjust(len(str(maior))), end='')
            else:
                print(str(matriz[i][j]).rjust(len(str(maior))), end=' ')
        imprimir_linha()


while True:
    entrada = int(input())
    if entrada == 0:
        break
    lista = matriz_quadrada(entrada)
    preencher_matriz(lista, entrada)
    imprimir_matriz(lista, entrada)
    imprimir_linha()
    lista.clear()
