import math
entrada = int(input())
p = entrada/math.log(entrada)
m = 1.25506 * (entrada / math.log(entrada))

print(f'{p:.1f} {m:.1f}')
