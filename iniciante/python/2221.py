# 2221.py
def valor_golpe(a, b, c, bonus):
    return (int(a) + int(b)) / 2 + (0, int(bonus))[int(c) % 2 == 0]


qtd_entrada = int(input())

while True:
    bonus = int(input())
    d_ai, d_di, d_li = input().split()
    g_ai, g_di, g_li = input().split()
    pomekon_dabriel = valor_golpe(d_ai, d_di, d_li, bonus)
    pomekon_guarte = valor_golpe(g_ai, g_di, g_li, bonus)

    if pomekon_dabriel > pomekon_guarte:
        print('Dabriel')
    elif pomekon_dabriel < pomekon_guarte:
        print('Guarte')
    else:
        print('Empate')
    qtd_entrada -= 1
    if not qtd_entrada:
        break
