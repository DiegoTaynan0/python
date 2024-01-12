# DESAFIO 008
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS.

m = int(input('Metros: '))

km = m * 0.0001
hm = m * 0.001
dam = m * 0.01
m = m * 1
dc = m * 10
cm = m * 100
mm = m * 1000

print('Quilometros: {} \nHectômetros: {} \nDecametros: {} \nMetros: {} \nDecímetros: {} \nCentímetros: {} \nMilímetros: {}' .format(km, hm, dam, m, dc, cm, mm))