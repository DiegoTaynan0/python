# DESAFIO 006
# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

nr = int(input('Digite um número: \n'))

dobro = nr * 2
triplo = nr * 3
raiz = nr **(1/2)

print('Número digitado: {} \nDobro: {} \nTriplo: {} \nRaiz quadrada: {}' .format(nr, dobro, triplo, raiz))
