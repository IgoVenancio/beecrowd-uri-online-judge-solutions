entrada = int(input()) - 1
denominador = 2.0
if entrada < 0:
    print('1.0000000000')
else:
    for _ in range(entrada):
        denominador = 2 + 1 / denominador
    print(f'{1 + 1 / denominador:.10f}')
