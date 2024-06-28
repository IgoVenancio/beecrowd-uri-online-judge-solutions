qtd_entrada = int(input())

while True:
    entrada = int(input())
    if entrada == 0:
        break

    if entrada % 2 == 0:
        print(entrada * 2 - 2)
    else:
        print(entrada * 2 - 1)

    qtd_entrada -= 1
    if qtd_entrada == 0:
        qtd_entrada = int(input())
        if qtd_entrada == 0:
            break
