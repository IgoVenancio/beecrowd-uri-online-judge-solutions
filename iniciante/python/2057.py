# -*- coding: utf-8 -*-

# Ordem de Entrada:
# - hora da saída 
# - tempo de viagem
# - fuso horario do destino com relação à origem

entrada = input().split()
hora_atual = (int(entrada[0]) + int(entrada[2]) + int(entrada[1]))
if hora_atual >= 24:
    print(hora_atual - 24)
elif hora_atual < 0:
    print(24 + hora_atual)
else:
    print(hora_atual)
