# -*- coding: utf-8 -*-

i = 1
j = 7
count = 0

while True:
    print(f'I={i} J={j}')
    if i == 9 and j == 5:
        break
    j -= 1
    count += 1
    if count == 3:
        i += 2 
        count = 0
        j = 7
