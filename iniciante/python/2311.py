qtd_entrada = int(input())
lista = []
soma_lista = 0

while True:
    nome = input()
    nota_entrada = float(input())
    lista_notas = input().split()
    lista_notas = [float(x) for x in lista_notas]
    lista_notas.sort()
    soma_lista = sum(lista_notas[1:-1])
    lista.append([nome, soma_lista * nota_entrada])
    qtd_entrada -= 1
    if not qtd_entrada:
        break

for resultado in lista:
    print(f'{resultado[0]} {resultado[1]:.2f}')
