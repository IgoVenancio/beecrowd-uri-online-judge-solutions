# -*- coding: utf-8 -*-

entrada = int(input())
while entrada != 0: 
    inicio1 = 0
    inicio2 = 0
    final1 = 0
    final2 = 0
    incremento = 1
    count_entradas = 0
    final1 = entrada
    final2 = entrada
    lista = [[0 for _ in range(entrada)] for _ in range(entrada)]
    while count_entradas < entrada:
        for i in range(inicio1, final1):
            for j in range(inicio2, final2):
                lista[i][j] = incremento
        incremento += 1
        inicio1 += 1
        inicio2 += 1
        final1 -= 1
        final2 -= 1
        count_entradas += 1

    for i in range(entrada):
        for j in range(entrada):
            if j == entrada - 1:
                print(str(lista[i][j]).rjust(3))
            else:
                print(str(lista[i][j]).rjust(3), end=' ')
    lista.clear()
    print()
    entrada = int(input())
