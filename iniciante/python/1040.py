# -*- coding: utf-8 -*-

entrada = input().split(' ')
entrada2 = 0.0

media = (float(entrada[0]) * 2 +
         float(entrada[1]) * 3 +
         float(entrada[2]) * 4 +
         float(entrada[3]) * 1) / 10
media2 = 0.0

print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    entrada2 = float(input())
    print(f'Nota do exame: {entrada2:.1f}')
    media2 = (entrada2 + media) / 2

    if media2 >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media2:.1f}')
