qtd_entrada = int(input())
paisagem = input().split()
paisagem_map = []
igual_nlogonia = 1

for x in range(len(paisagem)):
    if x == len(paisagem) - 1:
        print(igual_nlogonia)
        break
    if int(paisagem[x]) > int(paisagem[x + 1]):
        paisagem_map.append('vale')
    elif int(paisagem[x]) < int(paisagem[x + 1]):
        paisagem_map.append('pico')
    else:
        igual_nlogonia = 0
        print(igual_nlogonia)
        break
    if len(paisagem_map) > 1:
        if paisagem_map[x] == paisagem_map[x - 1]:
            igual_nlogonia = 0
            print(igual_nlogonia)
            break
