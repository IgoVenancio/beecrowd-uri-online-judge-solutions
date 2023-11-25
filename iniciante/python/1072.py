# -*- coding: utf-8 -*-

intervalo = range(10, 21)
count_entrada = 0
entrada = 0
count_dentro_intervalo = 0
count_fora_intervalo = 0

qtd_entrada = int(input())

while count_entrada < qtd_entrada:
    entrada = int(input())
    if entrada in intervalo:
        count_dentro_intervalo += 1
    else:
        count_fora_intervalo += 1
    count_entrada += 1

print(f'{count_dentro_intervalo} in')
print(f'{count_fora_intervalo} out')
