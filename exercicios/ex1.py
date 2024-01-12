import pandas as pd
import math

# importar a base de dados
tabeladevendas = pd.read_excel("expy/Vendas.xlsx")

# visualizar a base de dados
#pd.set_option('display.max_columns', None)

# faturamento por loja
faturamento = tabeladevendas [['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
#print(faturamento)

# quantidade de produtos vendidos por loja
quantidade_produtos = tabeladevendas [['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(quantidade_produtos)

# ticket médio do porduto em cada loja
ticket_medio = format(faturamento['Valor Final'] / quantidade_produtos['Quantidade'], '2f').to_frame()
print(ticket_medio)

# enviar um email com o relatório

