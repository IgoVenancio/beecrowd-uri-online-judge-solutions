# -*- coding: utf-8 -*-

contador = 0
while True:
    try:
        contador += 1
        tupla = tuple()
        entrada = int(input())
        for x in range(entrada + 1):
            if x == 0:
                tupla += x,
                continue
            tupla += (x,) * x
        print(f'Caso {contador}: {len(tupla)} '
              + ('numero', 'numeros')[entrada > 0])
        print(*tupla)
        print()
    except EOFError:
        break
