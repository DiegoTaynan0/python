# DESAFIO 011
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE SUA AREA E A QUANTIDADE DE TINTA NECESSÁRIA
# PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M².

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

area = altura * largura

litro = area / 2


print('Sua parede tem uma área de {}m², com isso precisa de {}l para pintar essa área.'.format(area, litro))
