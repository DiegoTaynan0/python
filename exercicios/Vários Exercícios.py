# Ex1 - Mostrar a mensagem
print('Olá, Mundo!')

# Ex2 - Ler número e mostrar a mensagem
nr = int(input('Digite um número? '))
print('Número digitado: ', nr)

# Ex3 - Soma de dois números
nr1 = int(input('Digite o nrº 1: '))
nr2 = int(input('Digite o nrº 2: '))

total = nr1 + nr2

print('Total: ', total)

#Ex4 - Ler quatro notas, calcular média e mostra-la
nr1 = int(input('Digite o nota 1: '))
nr2 = int(input('Digite o nota 2: '))
nr3 = int(input('Digite o nota 3: '))
nr4 = int(input('Digite o nota 4: '))

valor_total_media = ((nr1 + nr2 + nr3 + nr4)/4)

print('Media das notas: ', valor_total_media)


#Ex5 - Transformar metros em centimentros
m = int(input('Metros: '))
cm = int(100)

valor_convertido = m * cm

print(m, 'Metro/s é igual a', valor_convertido, 'Centímetros')

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