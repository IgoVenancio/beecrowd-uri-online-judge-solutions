while True:
    entrada = int(input())
    if entrada < 0:
        break
    print((entrada-1, entrada)[entrada == 0])
