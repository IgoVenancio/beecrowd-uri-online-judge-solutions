while True:
    try:
        entrada = input().split()
        entrada = [int(x) for x in entrada]

        # distancia ab = raiz((x2 - x1)^2 + (y2 - y1)^2)
        distancia = ((entrada[2] - entrada[0]) ** 2 +
                     (entrada[3] - entrada[1]) ** 2) ** (1/2)
        
        # R1 + R2 >= Distancia inicial + distancia final
        if entrada[5] + entrada[6] >= distancia + entrada[4] * 1.5:
            print('Y')
        else:
            print('N')
    except EOFError:
        break
