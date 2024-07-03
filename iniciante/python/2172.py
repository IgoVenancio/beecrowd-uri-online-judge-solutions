while True:
    entrada = input().split()
    if int(entrada[0]) == int(entrada[1]) == 0:
        break
    print(int(entrada[0]) * int(entrada[1]))
