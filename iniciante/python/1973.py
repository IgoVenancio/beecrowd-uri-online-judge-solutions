# -*- coding: utf-8 -*-
from sys import stdin


def main():
    qtd_estrelas = int(stdin.readline())
    estrelas = list(map(int, stdin.readline().split()))
    qtd_carneiros_roubados = sum(estrelas)
    posicao_atual = 0
    estrelas_atacadas = [0] * qtd_estrelas
    resultado = False

    while posicao_atual >= 0 and posicao_atual < qtd_estrelas:

        if estrelas[posicao_atual] % 2 == 0:
            resultado = True
        else:
            resultado = False

        if estrelas[posicao_atual] > 0:
            estrelas[posicao_atual] -= 1
            qtd_carneiros_roubados -= 1
            estrelas_atacadas[posicao_atual] = 1

        if resultado:
            posicao_atual -= 1
        else:
            posicao_atual += 1

    print(estrelas_atacadas.count(1), qtd_carneiros_roubados)


if __name__ == "__main__":
    main()
