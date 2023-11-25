# -*- coding: utf-8 -*-

maior = 0
posicao = 0
count_entrada = 0
while count_entrada < 100:
    entrada = int(input())
    if entrada > maior:
        maior = entrada
        posicao = count_entrada + 1

    count_entrada += 1

print(maior)
print(posicao)
