entrada = int(input())

resultado = (((1 + 5 ** (1/2)) / 2)**entrada -
             ((1 - 5 ** (1/2)) / 2)**entrada)/(5**(1/2))
print(f'{resultado:.1f}')
