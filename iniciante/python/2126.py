# -*- coding: utf-8 -*-

count_casos = 0
while True:
    count_casos += 1
    posicao = 0
    qtd_subsequencias = 0
    try:
        entrada1 = input()
        entrada2 = input()
        qtd_subsequencias = entrada2.count(entrada1)
        posicao = entrada2.rfind(entrada1)

        print(f'Caso #{count_casos}:')
        if qtd_subsequencias:
            print(f'Qtd.Subsequencias: {qtd_subsequencias}')
            print(f'Pos: {posicao + 1}')
        else:
            print('Nao existe subsequencia')
        print()

    except EOFError:
        break
