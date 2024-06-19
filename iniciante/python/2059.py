# -*- coding: utf-8 -*-

entrada = input().split()

jogador_1_vence = (False, True)[
    # Escolheu par nao roubou e nao foi acusado
    (int(entrada[0]) == 1 and 
     (int(entrada[1]) + int(entrada[2])) % 2 == 0 and
     (int(entrada[3]) + int(entrada[4])) == 0) or

    # Escolheu impar nao roubou e nao foi acusado
    (int(entrada[0]) == 0 and
     (int(entrada[1]) + int(entrada[2])) % 2 != 0 and
     (int(entrada[3]) + int(entrada[4])) == 0) or

    # Roubou independente do resultado
    (int(entrada[3]) == 1 and int(entrada[4]) == 0) or

    # Não roubou e foi acusado
    (int(entrada[3]) == 0 and int(entrada[4]) == 1)

]

if jogador_1_vence:
    print('Jogador 1 ganha!')
else:
    print('Jogador 2 ganha!')
