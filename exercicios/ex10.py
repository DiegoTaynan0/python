# DESAFIO 010
# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
# CONSIDERE US$1.00 = R$3.27

saldo =float(input('Saldo em conta: \n'))

dolar = 3.27

print('Pode comprar US${:.2f}' .format(saldo / dolar))