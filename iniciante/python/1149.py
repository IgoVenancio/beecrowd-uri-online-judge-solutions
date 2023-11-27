# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada = [int(x) for x in entrada]
a = entrada[0]
b = 0
soma = 0
for x in entrada[1:]:
    if x > 0:
        b = x
        break

for x in range(entrada[0], 0, -1):
    soma += x
for x in range(0, b):
    soma += x
print(soma)
