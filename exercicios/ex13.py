# DESAFIO 013
# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.

salario = float(input('Qual seu salário: '))

result = (salario * 0.15) + salario

print('Salario atual R${} \nSalario 15% de aumento: R${}' .format(salario, result))

