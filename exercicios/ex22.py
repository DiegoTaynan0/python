# DESAFIO 022
# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# - O NOME COM TODAS AS LETRAS MAIÚSCULAS
# - O NOME COM TODAS MINÚSCULAS
# - QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
# - QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = 'Diego Taynan Moura Lima'

dividir = nome.split()

print('Letras maiúsculas:', nome.upper())
print('Letras minúsculas:', nome.lower())
print('Quantas letras ao todo, sem considerar os espaços:', len(nome.strip()))
print('Dividir:', dividir[0])
