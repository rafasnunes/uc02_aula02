# Exemplo de cálculo de médias utilizando a biblioteca Numpy

import numpy as np

dados_salario = [2000, 2500, 3000, 3500, 4000, 30000]

media = np.mean(dados_salario) # Calculo de média simples - Soma dos valores dividido pela quantidade de valores.
print('Média: ', media)

mediana = np.median(dados_salario) # Calculo da mediana (Os dados precisam estar numa lista ordenada)
print('Mediana: ', mediana)