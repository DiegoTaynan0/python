# DESAFIO 017
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO
# RETÂNGULO. CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

from math import hypot

a = float(input('A: '))
b = float(input('B: '))

print('C: {:.2f}'.format(hypot(a, b)))