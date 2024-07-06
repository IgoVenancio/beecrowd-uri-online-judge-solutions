def triangulo_retangulo(a, b, c):
    lista = [a, b, c]
    lista = [int(x) for x in lista]
    lista.sort()
    return lista[2] ** 2 == lista[1] ** 2 + lista[0] ** 2


def triangulo_escaleno(a, b, c):
    return int(a) != int(b) and int(b) != int(c)


def triangulo_equilatero(a, b, c):
    return int(a) == int(b) == int(c)


def triangulo_isoceles(a, b, c):  
    return (int(a) == int(b) and int(a) != int(c)) or\
            (int(a) == int(c) and int(a) != int(b)) or \
            (int(b) == int(c) and int(b) != int(a))


def forma_triangulo(a, b, c):
    return abs(int(b) - int(c)) < int(a) < int(b) + int(c) or \
           abs(int(a) - int(c)) < int(b) < int(a) + int(c) or \
           abs(int(a) - int(b)) < int(c) < int(a) + int(b)


a, b, c = input().split()
# triângulo ?
if not forma_triangulo(a, b, c):
    print('Invalido')
else:
    # isoceles
    if triangulo_isoceles(a, b, c):
        print('Valido-Isoceles')
        print('Retangulo: ' + ('S', 'N')[not triangulo_retangulo(a, b, c)])
    # escaleno
    elif triangulo_escaleno(a, b, c):
        print('Valido-Escaleno')
        print('Retangulo: ' + ('S', 'N')[not triangulo_retangulo(a, b, c)])
    # equilatero
    else: 
        print('Valido-Equilatero')
        print('Retangulo: ' + ('S', 'N')[not triangulo_retangulo(a, b, c)])
