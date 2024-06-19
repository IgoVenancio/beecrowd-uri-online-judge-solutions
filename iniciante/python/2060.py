# -*- coding: utf-8 -*-

qtd_numeros = int(input())
lista = input().split()

multiplos_2 = 0
multiplos_3 = 0
multiplos_4 = 0
multiplos_5 = 0

for numero in lista:
    # multiplos de 2
    multiplos_2 += 1 if int(numero) % 2 == 0 else 0
    # multiplos de 3
    multiplos_3 += 1 if int(numero) % 3 == 0 else 0
    # multiplos de 4
    multiplos_4 += 1 if int(numero) % 4 == 0 else 0
    # multiplos de 5
    multiplos_5 += 1 if int(numero) % 5 == 0 else 0

print(f'{multiplos_2} Multiplo(s) de 2')
print(f'{multiplos_3} Multiplo(s) de 3')
print(f'{multiplos_4} Multiplo(s) de 4')
print(f'{multiplos_5} Multiplo(s) de 5')
