# -*- coding: utf-8 -*-

centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
dezenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


entrada = int(input())
cent = int(entrada/100)
entrada -= cent * 100
dez = int(entrada/10)
entrada -= dez * 10
un = entrada

print(f'{centenas[cent]}{dezenas[dez]}{unidades[un]}')
