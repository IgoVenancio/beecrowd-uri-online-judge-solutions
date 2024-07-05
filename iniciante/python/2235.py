entrada = input().split()
entrada = [int(x) for x in entrada]
a, b, c = entrada

if a == b + c or b == c + a or c == a + b or a == c or a == b or b == c or a == c:
    print('S')
else:
    print('N')
