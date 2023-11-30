# -*- coding: utf-8 -*-

entrada = input().split(' ')
dia1 = int(entrada[0])
dia2 = int(entrada[1])
dia3 = int(entrada[2])

if dia2 < dia1 and dia3 >= dia2:
    print(':)')
elif dia2 > dia1 and dia3 <= dia2:
    print(':(')
elif dia2 > dia1 and dia3 > dia2 and ((dia3 - dia2) < (dia2 - dia1)):
    print(':(')
elif dia2 > dia1 and dia3 > dia2 and ((dia3 - dia2) >= (dia2 - dia1)):
    print(':)')
elif dia2 < dia1 and dia3 < dia2 and ((dia2 - dia3) < (dia1 - dia2)):
    print(':)')
elif dia2 < dia1 and dia3 < dia2 and ((dia2 - dia3) >= (dia1 - dia2)):
    print(':(')
elif dia2 == dia1 and dia3 > dia2:
    print(':)')
elif dia2 == dia1 and dia3 < dia2:
    print(':(')
elif dia2 == dia1 and dia3 == dia2:
    print(':(')
