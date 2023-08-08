'''
1.
fatorial
numero

2.
Pegar o numero digitado e multiplicar por todos números antecessores a ele.

3.
Não é permitido número negativos

4.
Que o usuario informe o numero que deseja descobrir o fatorial e o sistema irá multiplicar por todos números que o antecedem e apresentar
o resultado.
'''

fatorial = 1
numero = int(input('Digite um número: '))

if numero >= 1:
    for i in range (1, numero +1):
        fatorial = i * fatorial
        print(fatorial)
else:
    print('Digite um número inteiro!')