# -*- coding: utf-8 -*-

count = 0
entrada = []
count_par = 0

while count < 5:
    entrada.append(int(input()))
    if entrada[count] % 2 == 0:
        count_par += 1
    count += 1

print(f'{count_par} valores pares')
