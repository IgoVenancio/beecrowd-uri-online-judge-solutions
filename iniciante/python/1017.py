# -*- coding: utf-8 -*-

AUTONOMIA_AUTOMOVEL = 12  # KM/L
tempo_viagem = int(input())
velocidade_media = int(input())
qtd_litros = (tempo_viagem * velocidade_media) / AUTONOMIA_AUTOMOVEL

print(f'{qtd_litros:.3f}')
