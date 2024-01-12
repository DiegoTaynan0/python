# DESAFIO 015
# ESCREVA UM PROGRAMA QUE PERGUNTA A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS
# QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0.15 POR KM RODADO.

diaria =  int(input('Quantos dias: '))
km = float(input('Quantos Km rodados: '))

a = diaria * 60
b = km * 0.15

print('Custará: \nDiaria R${} \nKilometragem R${:.2f} \nTotal: {:.2f}'.format(a, b, a+b))
