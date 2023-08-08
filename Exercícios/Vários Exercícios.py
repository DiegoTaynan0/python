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
