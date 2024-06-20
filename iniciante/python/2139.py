# -*- coding: utf-8 -*-

def qtd_dias_ate_natal(mes, dia):
    qtd_dias = 0
    lista_dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]
    for m in range(mes - 1, 12):
        qtd_dias += lista_dias[m]
    
    qtd_dias -= dia
    return qtd_dias


while True:
    try:
        entrada = input().split()
        if entrada == ['12', '25']:
            print('E natal!')
        elif entrada[0] == '12' and int(entrada[1]) > 25:
            print('Ja passou!')
        elif entrada[0] == '12' and int(entrada[1]) == 24:
            print('E vespera de natal!')
        else:
            print(f'Faltam {qtd_dias_ate_natal(int(entrada[0]), int(entrada[1]))} dias para o natal!')

    except EOFError:
        break
