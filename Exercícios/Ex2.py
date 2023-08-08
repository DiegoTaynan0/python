'''
Imprima numeros de forma crescente de 1 a N.

1. 
valor_base
valor_n

2.
Usuário deve digitar um numero aleatório, o sistema irá verificar se esse número é inteiro, se sim, ele irá imprimir número 1
até o número que o usuário digitou, se não, irá informar que só aceita número inteiros.

3. Não é permitido digitar números negativos ou igual ao número base.

4. Que o sistema imprima os números de forma crescente.   
'''

valor_inicial = 1
valor_n = int(input('Digite um numero: '))
if valor_n < 1:
    print('Digite um número inteiro!')

elif valor_n <= valor_inicial:
    print('Valor digitado é menor ou igual o número inicial! \n' 'Tente Novamente!!')

else:
    for i in range (valor_inicial,valor_n):
        print(i)