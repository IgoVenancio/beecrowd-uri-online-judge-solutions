# -*- coding: utf-8 -*-

def criar_matriz(dimensao, default=0):
    return [[default for _ in range(dimensao)] for _ in range(dimensao)]


def preencher_diagonal_principal(matriz, dimensao, valor):
    for i in range(dimensao):
        matriz[i][i] = valor

def preencher_diagonal_secundaria(matriz, dimensao, valor):
    for i in range(dimensao):
        matriz[i][dimensao - 1 - i] = valor


def preencher_matriz_interna(matriz, dimensao):
    dimensao_nova = int(dimensao/3)
    for i in range(dimensao_nova, (dimensao - dimensao_nova)):
        for j in range(dimensao_nova, (dimensao - dimensao_nova)):
            matriz[i][j] = 1


def imprimir_linha():
    print()


def imprimir_matriz(matriz, dimensao):
    for i in range(dimensao):
        for j in range(dimensao):
            print(matriz[i][j], end='')
        imprimir_linha()


def preencher_central(matriz, dimensao, valor):
    central_matriz = int((dimensao - 1)/2)
    matriz[central_matriz][central_matriz] = valor


while True:
    try:
        entrada = int(input())
        lista = criar_matriz(entrada)
        preencher_diagonal_principal(lista, entrada, 2)
        preencher_diagonal_secundaria(lista, entrada, 3)
        preencher_matriz_interna(lista, entrada)
        if entrada % 2 != 0:
            preencher_central(lista, entrada, 4)
        imprimir_matriz(lista, entrada)
        imprimir_linha()
        lista.clear()
    except EOFError:
        break
