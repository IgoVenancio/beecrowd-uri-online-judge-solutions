# -*- coding: utf-8 -*-

entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
q = 0

for resto in range(abs(b)):
    q = int((a - resto)/b)
    if a == (b * q + resto):
        break
print(q, resto)
