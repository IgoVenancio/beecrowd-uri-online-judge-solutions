# -*- coding: utf-8 -*-

qtd_entrada = int(input())

inscricao_nota = []
for x in range(qtd_entrada):
    entrada = input().split()
    inscricao_nota.append({'inscricao': entrada[0], 'nota': float(entrada[1])})

inscricao_nota.sort(key=lambda x: x['nota'])
print(inscricao_nota[-1]['inscricao'] if inscricao_nota[-1]['nota'] >= 8.0 
      else 'Minimum note not reached')
