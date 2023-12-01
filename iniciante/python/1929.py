# -*- coding: utf-8 -*-

entrada = input().split(' ')
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
d = int(entrada[3])

if a + b > c and b + c > a and a + c > b: # a b c
    print('S')
elif a + b > d and b + d > a and a + d > b: # a b d
    print('S')
elif a + c > d and c + d > a and a + d > c: # a c d
    print('S')
elif b + c > a and b + a > c and c + a > b: # b c a
    print('S')
elif b + d > a and b + a > d and d + a > b: # b d a
    print('S')
elif b + c > d and c + d > b and b + d > c: # b c d
    print('S')
else:
    print('N')
