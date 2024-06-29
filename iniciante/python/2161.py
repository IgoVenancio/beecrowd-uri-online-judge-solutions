entrada = int(input()) - 1
denominador = 6.0
if entrada < 0:
    print('3.0000000000')
else:
    for _ in range(entrada):
        denominador = 6 + 1 / denominador
    print(f'{3 + 1 / denominador:.10f}')
