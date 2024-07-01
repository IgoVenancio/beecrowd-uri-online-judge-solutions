qtd_velocidade = int(input())
velocidades = input().split()

for x in range(qtd_velocidade):
    if x != 0:
        if int(velocidades[x]) < int(velocidades[x - 1]):
            print(x + 1)
            break
else:
    print(0)
