# -*- coding: utf-8 -*-

def matriz_quadrada(dimensao):
    return [[3 for _ in range(dimensao)] for _ in range(dimensao)]


def preencher_diagonal_principal(matriz, dimensao, valor):
    for i in range(dimensao):
        matriz[i][i] = valor


def preencher_diagonal_secundaria(matriz, dimensao, valor):
    j = dimensao - 1
    for i in range(dimensao):
        matriz[i][j] = valor
        j -= 1


def imprimir_linha():
    print()


def imprimir_lista(matriz, dimensao):
    for i in range(dimensao):
        for j in range(dimensao):
            print(matriz[i][j], end='')
        if j == dimensao - 1:
            imprimir_linha()


while True:
    try:
        entrada = input()
        lista = matriz_quadrada(int(entrada))
        preencher_diagonal_principal(lista, int(entrada), 1)
        preencher_diagonal_secundaria(lista, int(entrada), 2)
        imprimir_lista(lista, int(entrada))
        lista.clear()
    except EOFError:
        break
