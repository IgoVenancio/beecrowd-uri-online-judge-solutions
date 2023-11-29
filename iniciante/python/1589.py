# -*- coding: utf-8 -*-

count_entrada = 0
entrada = int(input())
while count_entrada < entrada:
    entrada2 = input().split(' ')
    print(int(entrada2[0]) + int(entrada2[1]))
    count_entrada += 1
