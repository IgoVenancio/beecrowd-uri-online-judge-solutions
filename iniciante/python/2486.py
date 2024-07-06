def main(): 
    tabela_nutricional = {
        'suco de laranja': 120,
        'morango fresco': 85,
        'mamao': 85,
        'goiaba vermelha': 70,
        'manga': 56,
        'laranja': 50,
        'brocolis':	34
    }

    while True:
        qtd_mg = 0
        qtd_entrada = int(input())
        if qtd_entrada == 0:
            break
        while True:
            entrada = input()
            chave = entrada[2:]
            valor = int(entrada.split()[0])
            qtd_mg += (tabela_nutricional[chave.strip()] * valor)
            qtd_entrada -= 1
            if not qtd_entrada:
                break
        if qtd_mg in range(110, 131):
            print(f'{qtd_mg} mg')
        elif qtd_mg < 110:
            print(f'Mais {abs(110 - qtd_mg)} mg')
        else:
            print(f'Menos {abs(qtd_mg - 130)} mg')


if __name__ == "__main__":
    main()
