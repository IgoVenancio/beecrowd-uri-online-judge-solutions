entrada = int(input())
matriz = []
matriz_mapeamento = []

for x in range(entrada + 1):
    matriz.append([])
    entrada_2 = input().split()
    for y in range(entrada + 1):
        matriz[x].append(int(entrada_2[y]))

for x in range(entrada + 1):
    if x == entrada:
        continue
    matriz_mapeamento.append([])
    for y in range(entrada + 1):
        if y == entrada or x == entrada:
            continue
        if matriz[x][y] + matriz[x][y + 1] + matriz[x + 1][y] + matriz[x + 1][y + 1] >= 2:
            matriz_mapeamento[x].append('S')
        else:
            matriz_mapeamento[x].append('U')

for mapa in matriz_mapeamento:
    print(*mapa, sep='')
