# -*- coding: utf-8 -*-

def fatorial(a):
    if a == 1:
        return 1
    else:
        return a * fatorial(a - 1)


entrada = int(input())
print(fatorial(entrada))
