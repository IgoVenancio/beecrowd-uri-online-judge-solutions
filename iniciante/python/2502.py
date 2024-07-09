while True:
    try:
        c, n = input().split()
        cifra_1 = input()
        cifra_2 = input()
        decode = dict()

        for x in range(int(c)):
            decode[cifra_1[x]] = cifra_2[x]
            decode[cifra_2[x]] = cifra_1[x]
            decode[cifra_1[x].lower()] = cifra_2[x].lower()
            decode[cifra_2[x].lower()] = cifra_1[x].lower()

        for _ in range(int(n)):
            frase = input().strip()
            for letra in frase:
                print(decode.get(letra, letra), end='')
            print()
        print()

    except EOFError:
        break
