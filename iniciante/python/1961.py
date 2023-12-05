# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada2 = input().split()
game_over = True

for i in range(len(entrada2) - 1):
    medida = int(entrada2[i + 1]) - int(entrada2[i])
    if abs(medida) > int(entrada[0]):
        print('GAME OVER')
        game_over = False
        break

if game_over:
    print('YOU WIN')
