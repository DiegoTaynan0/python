# DESAFIO 018
# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.

from math import sin, cos, tan, radians

angulo = float(input('Ângulo: '))

print('Seno: {:.2f}'.format(sin(radians(angulo))))
print('Cosseno: {:.2f}'.format(cos(radians(angulo))))
print('Tangente: {:.2f}'.format(tan(radians(angulo))))
