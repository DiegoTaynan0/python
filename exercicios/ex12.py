# DESAFIO 012
# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

preco = float(input('Preço do produto: '))

result = (preco * 5) / 100

print('Preço: {} \nPreco com desconto: {}' .format(preco, result))
