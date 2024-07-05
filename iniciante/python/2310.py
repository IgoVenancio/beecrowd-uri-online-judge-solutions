qtd_entrada = int(input())
saque = 0
bloqueio = 0
ataque = 0
pontos_saque = 0
pontos_bloqueio = 0
pontos_ataque = 0

while True:
    nome = input()
    a, b, c = input().split()
    d, e, f = input().split()
    saque += int(a)
    bloqueio += int(b)
    ataque += int(c)
    pontos_saque += int(d)
    pontos_bloqueio += int(e)
    pontos_ataque += int(f)

    qtd_entrada -= 1
    if not qtd_entrada:
        break

print(f'Pontos de Saque: {(pontos_saque / saque * 100):.2f} %.')
print(f'Pontos de Bloqueio: {(pontos_bloqueio / bloqueio * 100):.2f} %.')
print(f'Pontos de Ataque: {(pontos_ataque / ataque * 100):.2f} %.')
