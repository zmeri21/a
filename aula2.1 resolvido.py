# Exercício 1 - Importação e exploração inicial de um CSV com Pandas



# Alterar o nome do ficheiro para o CSV fornecido pela turma


# Importa o ficheiro para um DataFrame
import pandas as pd
df = pd.read_csv("C:/Users/Administrador/Downloads/data1.csv")

# Visualiza as 5 primeiras linhas
print(df.head(5))


# Visualiza as 5 últimas linhas
print(df.tail(5))


# Mostra o número de linhas e colunas
print(df.shape)


# Mostra informações dos tipos de dados das colunas e valores nulos
print(df.axes)


# Mostra estatísticas descritivas das colunas numéricas
print(df.describe())


