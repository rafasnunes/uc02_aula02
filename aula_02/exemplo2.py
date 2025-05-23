import pandas as pd

# Instalar a biblioteca openpyxl para ler arquivos de Excel
# Comando: pip install openpyxl

# Comando para criar uma snapshot das bibliotecas utilizadas e versões:
# pip freeze > requirements.txt

df = pd.read_excel('vendas_eletronicos.xlsx')

print(df.head())

# Valor máximo de faturamento total
# Utilizar o índice existente para imprimir o valor

print('\nMaior valor de faturamento total:')
print(df['Faturamento Total (R$)'].max())