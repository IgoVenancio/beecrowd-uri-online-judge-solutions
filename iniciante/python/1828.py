# -*- coding: utf-8 -*-

lista = [['tesoura', 'papel'],
         ['papel', 'pedra'],
         ['pedra', 'lagarto'],
         ['lagarto', 'Spock'],
         ['Spock', 'tesoura'],
         ['tesoura', 'lagarto'],
         ['lagarto', 'papel'],
         ['papel', 'Spock'],
         ['Spock', 'pedra'],
         ['pedra', 'tesoura']]

count_entrada = 1
entrada = int(input())
while count_entrada <= entrada:
    entrada2 = input().split(' ')
    if entrada2[0] == entrada2[1]:
        print(f'Caso #{count_entrada}: De novo!')
    else:
        if entrada2 in lista:
            print(f'Caso #{count_entrada}: Bazinga!')
        else:
            print(f'Caso #{count_entrada}: Raj trapaceou!')
    count_entrada += 1
