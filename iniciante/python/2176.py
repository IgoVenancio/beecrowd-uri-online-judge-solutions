mensagem = input()
numero_1 = 0
numero_0 = 0

for valor in mensagem:
    if int(valor) == 0:
        numero_0 += 1
    else:
        numero_1 += 1

if numero_1 % 2 != 0:
    mensagem += '1'
elif numero_1 % 2 == 0:
    mensagem += '0'

print(mensagem)
