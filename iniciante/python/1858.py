# -*- coding: utf-8 -*-

entrada = int(input())
entrada2 = input().split(' ')
entrada2 = [int(x) for x in entrada2]
entrada2_crescente = sorted(entrada2)
print(entrada2.index(entrada2_crescente[0]) + 1)
