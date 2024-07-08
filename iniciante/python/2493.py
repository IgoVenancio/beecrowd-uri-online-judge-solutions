def verificar_impossivel(numero_a, numero_b, numero_c):
    if (numero_a + numero_b) == numero_c:
        return True
    if (numero_a - numero_b) == numero_c:
        return True
    if (numero_a * numero_b) == numero_c:
        return True
    return False


def operacao(numero_a, numero_b, operador):
    if operador == '+':
        return numero_a + numero_b
    if operador == '-':
        return numero_a - numero_b
    if operador == '*':
        return numero_a * numero_b


def acertou_miseravi(lista_teste, lista_resposta, tamanho):
    lista_resultado = []
    for x in range(tamanho):
        nome, posicao, operador = lista_resposta[x].split(' ')

        # Substring Teste
        teste = lista_teste[int(posicao) - 1].split(' ')
        numero_1 = int(teste[0])
        numero_2 = int(teste[1].split('=')[0])
        numero_3 = int(teste[1].split('=')[1])

        # Teste
        if operador != 'I':
            if numero_3 != operacao(numero_1, numero_2, operador):
                lista_resultado.append(nome)
        else:
            if verificar_impossivel(numero_1, numero_2, numero_3):
                lista_resultado.append(nome)

    return lista_resultado


while True:
    try:
        lista_testes = []
        lista_respostas = []
        qtd_testes = int(input())

        # Testes
        for _ in range(qtd_testes):
            lista_testes.append(input())

        # Jogadores e respostas
        for _ in range(qtd_testes):
            lista_respostas.append(input())

        # Validação das escolhas
        errou = acertou_miseravi(lista_testes, lista_respostas, qtd_testes)

        # Respostas possíveis
        # Ninguém venceu
        if len(errou) == qtd_testes:
            print('None Shall Pass!')

        # Todos venceram
        elif len(errou) == 0:   
            print('You Shall All Pass!')

        # Jogadores que erraram em ordem lexicográfica
        else:
            print(*sorted(errou))

    except EOFError:
        break
