# Exemplo utilizando Quartil

import numpy as np
import pandas as pd

idade = np.array([35, 25, 38, 31, 45, 22, 36, 29, 40, 32])

q1 = np.quantile(idade, 0.25)
q2 = np.quantile(idade, 0.50)
q3 = np.quantile(idade, 0.75)

print('Q1: ', q1)
print('Q2: ', q2)
print('Q3: ', q3)

media = np.mean(idade)
print('Media: ', media)

mediana = np.median(idade)
print('Mediana: ', mediana)