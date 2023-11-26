# -*- coding: utf-8 -*-

inter = 0
gremio = 0
empate = 0
entrada = ''
entrada2 = 0
count_grenais = 0

while True:
    entrada = input().split(' ')
    if int(entrada[0]) > int(entrada[1]):
        inter += 1
    elif int(entrada[0]) == int(entrada[1]):
        empate += 1
    else:
        gremio += 1

    while True:
        print('Novo grenal (1-sim 2-nao)')
        entrada2 = int(input())
        break
    count_grenais += 1
    if entrada2 == 2:
        break

print(f'{count_grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')

if inter > gremio:
    print('Inter venceu mais')
elif inter < gremio:
    print('Gremio vvenceu mais')
else:
    print('Nao houve vencedor')
