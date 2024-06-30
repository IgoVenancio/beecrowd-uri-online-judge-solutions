def main():
    linhas_colunas = input().split()
    area_varredura = []
    posicao = [0, 0]

    # Preencher matriz
    for x in range(int(linhas_colunas[0])):
        area_varredura.append([])
        entrada_linha = input().split()
        for y in range(int(linhas_colunas[1])):
            area_varredura[x].append(int(entrada_linha[y]))

    # Procurar o sabre
    for x in range(int(linhas_colunas[0])):
        for y in range(int(linhas_colunas[1])):
            if x == 0 or x == int(linhas_colunas[0]) - 1 or \
               y == 0 or y == int(linhas_colunas[1]) - 1:
                continue

            if area_varredura[x - 1][y] == area_varredura[x + 1][y] == \
               area_varredura[x][y + 1] == area_varredura[x][y - 1] == \
               area_varredura[x - 1][y + 1] == area_varredura[x - 1][y - 1] == \
               area_varredura[x + 1][y + 1] == area_varredura[x - 1][y - 1] == 7 \
               and area_varredura[x][y] == 42:
                posicao[0] = x + 1
                posicao[1] = y + 1
                break
        else:
            continue
        break

    print(*posicao)


if __name__ == "__main__":
    main()
