# DESAFIO 0014
# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADAEM ºC E CONVERTA PARA ºF.

c = float(input('ºC: '))

result = (c * 1.8) + 32

print('{}ºC equivale a {:.1f}ºF'.format(c, result))