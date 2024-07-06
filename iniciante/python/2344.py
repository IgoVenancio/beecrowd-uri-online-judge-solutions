entrada = int(input())

if entrada == 0:
    print('E')
elif entrada in range(1, 36):
    print('D')
elif entrada in range(36, 61):
    print('C')
elif entrada in range(61, 85):
    print('B')
else:
    print('A')
