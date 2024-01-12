# DESAFIO 004
# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.

n = input('Digite algo: ')
print('Qual tipo?', type(n))
print('É um numérico?', n.isnumeric())
print('É alfanumérico?', n.isalpha())
print('É ASCII?', n.isascii())
print('É decimal?', n.isdecimal())
print('É um digito?', n.isdigit())
print('É identificador?', n.isidentifier())
print('Esta maiúsculo?', n.isupper())
print('Esta minúsculo?', n.islower())

            