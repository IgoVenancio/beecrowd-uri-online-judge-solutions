# -*- coding: utf-8 -*-

count = 0
entrada = []
count_par = 0
count_impar = 0
count_positivo = 0
count_negativo = 0

while count < 5:
    entrada.append(int(input()))
    if entrada[count] > 0:
        count_positivo += 1
    else:
        if entrada[count] != 0:
            count_negativo += 1
    if entrada[count] % 2 == 0:
        count_par += 1
    else:
        count_impar += 1

    count += 1

print(f'{count_par} valor(es) par(es)')
print(f'{count_impar} valor(es) impar(es)')
print(f'{count_positivo} valor(es) positivo(s)')
print(f'{count_negativo} valor(es) negativo(s)')
