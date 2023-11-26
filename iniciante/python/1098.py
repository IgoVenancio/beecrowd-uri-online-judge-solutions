# -*- coding: utf-8 -*-

i = 0
j = 1
count = 0
count2 = 0

while count2 < 33:
    if i == 0 or i == 1.0 or i == 1.9999999999999998:  
        print(f'I={i:.0f} J={(i+j):.0f}')
    else:
        print(f'I={i:.1f} J={(i+j):.1f}')
    j += 1
    count += 1 
    if count == 3:
        i += 0.2
        j = 1
        count = 0
    count2 += 1
