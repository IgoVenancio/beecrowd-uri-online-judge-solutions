# -*- coding: utf-8 -*-

jogador_vence = [
                ['ataque', 'pedra'],
                ['pedra', 'papel'],
                ['ataque', 'papel'],
                ]

qtd_jogadas = int(input())
while True:
    jogada_1 = input()
    jogada_2 = input()

    if [jogada_1, jogada_2] in jogador_vence:
        print('Jogador 1 venceu')
    elif [jogada_2, jogada_1] in jogador_vence:
        print('Jogador 2 venceu')
    elif [jogada_1, jogada_2] == ['ataque', 'ataque']:
        print('Aniquilacao mutua')
    elif [jogada_1, jogada_2] == ['papel', 'papel']:
        print('Ambos venceram')
    else:
        print('Sem ganhador')

    qtd_jogadas -= 1
    if qtd_jogadas == 0:
        break
