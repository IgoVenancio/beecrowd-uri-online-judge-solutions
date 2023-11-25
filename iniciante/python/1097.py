# -*- coding: utf-8 -*-

i = 1
j = 7
count = 0
inicial = 7

while True:
    print(f'I={i} J={j}')
    if i == 9 and j == 13:
        break
    j -= 1
    count += 1
    if count == 3:
        i += 2 
        count = 0
        j = inicial + 2
        inicial = j
