qtd_entrada = int(input())

while True:
    entrada = len(input())

    print(f'{(entrada / 100):.2f}')
    qtd_entrada -= 1
    if not qtd_entrada:
        break
