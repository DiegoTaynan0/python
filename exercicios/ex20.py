# DESAFIO 020
# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS
# E MOSTRE A ORDEM SORTEADA.

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))

lista = [aluno1, aluno2, aluno3, aluno4]

print('Lista ordenada: {}'.format(sorted(lista)))