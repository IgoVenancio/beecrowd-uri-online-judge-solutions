# -*- coding: utf-8 -*-

entrada = int(input())

valor_entrada = entrada
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

while True:
    if entrada >= 100:
        cem += 1 
        entrada -= 100
    elif entrada >= 50:
        cinquenta += 1
        entrada -= 50
    elif entrada >= 20:
        vinte +=1
        entrada -= 20
    elif entrada >= 10:
        dez += 1
        entrada -= 10
    elif entrada >= 5:
        cinco += 1
        entrada -= 5
    elif entrada >= 2:
        dois += 1
        entrada -= 2
    elif entrada >= 1:
        um += 1
        entrada -= 1
    else:
        break
print(valor_entrada)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')
