operacao = input()
soma = 0
lista = []
linha = 11
inicio = 1
final = 11
count_numeros = 0


for i in range(12):
    lista.append([])
    for j in range(12):
        entrada = input()
        if '.' in entrada:
            entrada = float(entrada)
        else:
            entrada = int(entrada)
        lista[i].append(entrada)

for j in range(5):
    for i in range(inicio, final):
        soma += lista[linha][i]
        count_numeros += 1
    inicio += 1
    final -= 1
    linha -= 1

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{(soma/count_numeros):.1f}')
