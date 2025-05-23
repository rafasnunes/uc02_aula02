# Uma imobiliária deseja analisar o valor "típico" das casas vendidas em um determinado mês para poder ajustar suas estratégias de vendas.
# Abaixo estão os valores de venda das 10 casas mais recentes:

# R$ 150.000 / R$ 280.000 / R$ 180.000 / R$ 200.000 / R$ 220.000
# R$ 300.000 / R$ 320.000 / R$ 400.000 / R$ 1.500.000 / R$ 250.000

# O gerente de vendas quer saber qual é o valor "mais representativo" das casas vendidas,
# ou seja, o valor típico da maioria das vendas, para definir uma faixa de preço para futuros clientes.

# 1. Calcule o valor médio de venda das casas.
# 2. Calcule o valor mediano das vendas.
# 3. Decida qual desses valores (média ou mediana) melhor representa o "valor típico" das casas vendidas.
# 4. Justifique sua resposta com base nos calculos.

import numpy as np

valores = [150000, 180000, 20000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000]

vlr_medio = np.mean(valores)
print(f'O valor médio das casas é R$ {vlr_medio:.2f}')

vlr_mediano = np.median(valores)
print(f'O valor mediano das casas é R$ {vlr_mediano:.2f}')


print('O valor típico de casas vendidas é melhor representado pela mediana, pois a maioria dos valores das casas vendidas está entre 150 e 400 mil')