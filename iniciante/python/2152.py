qtd_entrada = int(input())

while True:
    entrada = input().split()
    if len(entrada[0]) == 1 and len(entrada[1]) == 2: 
        print(f'0{entrada[0]}:{entrada[1]} - A porta '
              + ('abriu!', 'fechou!')[int(entrada[2]) == 0])
    elif len(entrada[0]) == 2 and len(entrada[1]) == 1: 
        print(f'{entrada[0]}:0{entrada[1]} - A porta '
              + ('abriu!', 'fechou!')[int(entrada[2]) == 0])
    elif len(entrada[0]) == 1 and len(entrada[1]) == 1: 
        print(f'0{entrada[0]}:0{entrada[1]} - A porta '
              + ('abriu!', 'fechou!')[int(entrada[2]) == 0])
    else:
        print(f'{entrada[0]}:{entrada[1]} - A porta '
              + ('abriu!', 'fechou!')[int(entrada[2]) == 0])

    qtd_entrada -= 1
    if not qtd_entrada:
        break
