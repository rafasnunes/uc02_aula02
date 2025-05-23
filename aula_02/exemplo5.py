# Você foi contratado como analista de vendas em uma loja de roupas e recebeu a tarefa de analisar os dados de vendas recentes.
# Seu gerente solicitou que você prepare um relatório contendo as seguintes informações a partir da planilha vendas _roupas. xIs:

# Produto: Nome dos itens vendidos.
# Quantidade Vendida: Total de unidades vendidas de cada produto.
# Preço por Unidade: Valor de venda de cada produto.
# Faturamento Total: Total gerado por cada produto vendido.
# Identificar os extremos do DataSet.
# Nível de Satisfação do Cliente: Avaliação dos clientes sobre os produtos.

# SUA TAREFA

# 1. Carregar os dados da planilha vendas roupas.xls utilizando o método read excel da biblioteca Pandas.
# 2. Exibir as 10 primeiras linhas do DataFrame, para uma visão geral dos dados.
# 3. Realizar as seguintes operações:
# 4. Calcular o somatório total das quantidades vendidas. 
# 5. Encontrar o valor médio dos preços por unidade.
# 6. Descobrir o maior faturamento total entre os produtos.
# 7. Identificar o menor faturamento total entre os produtos.
# 8. Identificar os produtos com classificação de nível de satisfação baixo.

import pandas as pd
import numpy as np

df = pd.read_excel('vendas_roupas.xlsx')
print(df.head(10))

# print(df.describe)

categoria = df['Categoria']
quantidade_vendida = df['Unidades Vendidas']

# print(quantidade_vendida)

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

print(media)
print(mediana)

# Organizar o DataFrame em ordem crescente pela quantidade vendida

quantidade_vendida = df.sort_values(by='Unidades Vendidas', ascending=False)


print(quantidade_vendida.values)

satisfacao = df[df['Satisfação'] == 'Baixo']
print(satisfacao)
