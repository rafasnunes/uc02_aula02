# Introdução a DataFrame
# Uma série é facilmente confundida com uma lista. Uma lista é uma coleção de dados
# DataFrame é uma tabela de dados composta por séries. Uma série é uma coluna de dados.

import pandas as pd
data = {
    'Nome' : ['Ana', 'João', 'Maria'],
    'Idade' : [23, 35, 29],
    'Gênero' : ['F', 'M', 'F'],
    'Altura' : [1.70, 1.80, 1.75],
    }


# Imprimir a coluna "Nome" - print(data['Nome'])

df_dados = pd.DataFrame(data)
print(df_dados)

# Printando variáveis quantitativas (Quantitativas = São Números)

print(df_dados['Idade'])

print(df_dados['Altura'])

# Printando variáveis quantitativas (Que são atributos não núméricos. Ex: Cor, Raça. Sexo, Etc.)

print(df_dados['Nome'])

print(df_dados['Gênero'])