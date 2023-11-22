# -*- coding: utf-8 -*-

entrada = input().split('.')
entrada[0] = int(entrada[0])
entrada[1] = int(entrada[1])

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
moeda_cinquenta = 0
moeda_vinte_e_cinco = 0
moeda_dez = 0
moeda_cinco = 0
moeda_um = 0


while True:
    if entrada[0] >= 100:
        cem += 1
        entrada[0] -= 100
    elif entrada[0] >= 50:
        cinquenta += 1
        entrada[0] -= 50
    elif entrada[0] >= 20:
        vinte += 1
        entrada[0] -= 20
    elif entrada[0] >= 10:
        dez += 1
        entrada[0] -= 10
    elif entrada[0] >= 5:
        cinco += 1
        entrada[0] -= 5
    elif entrada[0] >= 2:
        dois += 1
        entrada[0] -= 2
    elif entrada[0] >= 1:
        um += 1
        entrada[0] -= 1
    else:
        break

while True:
    if entrada[1] >= 50:
        moeda_cinquenta += 1
        entrada[1] -= 50
    elif entrada[1] >= 25:
        moeda_vinte_e_cinco += 1
        entrada[1] -= 25
    elif entrada[1] >= 10:
        moeda_dez += 1
        entrada[1] -= 10
    elif entrada[1] >= 5:
        moeda_cinco += 1
        entrada[1] -= 5
    elif entrada[1] >= 1:
        moeda_um += 1
        entrada[1] -= 1
    else:
        break

print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cinquenta} nota(s) de R$ 50.00')
print(f'{vinte} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')
print(f'{cinco} nota(s) de R$ 5.00')
print(f'{dois} nota(s) de R$ 2.00')


print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1.00')
print(f'{moeda_cinquenta} moeda(s) de R$ 0.50')
print(f'{moeda_vinte_e_cinco} moeda(s) de R$ 0.25')
print(f'{moeda_dez} moeda(s) de R$ 0.10')
print(f'{moeda_cinco} moeda(s) de R$ 0.05')
print(f'{moeda_um} moeda(s) de R$ 0.01')
