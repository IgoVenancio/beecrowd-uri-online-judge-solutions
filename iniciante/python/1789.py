# -*- coding: utf-8 -*-

while True:
    try:
        entrada = int(input())
        entrada2 = input().split(' ')
        entrada2 = [int(x) for x in entrada2]
        entrada2.sort(reverse=True)
        if entrada2[0] < 10:
            print(1)
        elif entrada2[0] >= 10 and entrada2[0] < 20:
            print(2)
        else:
            print(3)

    except EOFError:
        break
