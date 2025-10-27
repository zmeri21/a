# Exercício 2 - Importação, junção de DataFrames e exportação



# Alterar os nomes dos ficheiros conforme os fornecidos à turma



# Importa os ficheiros para DataFrames
import pandas as pd
df1 = pd.read_csv("C:/Users/Administrador/Downloads/clientes.csv")
df2 = pd.read_csv("C:/Users/Administrador/Downloads/vendas.csv", sep=';', decimal=',')

# Faz merge pelo campo 'cliente_id'
dfMerged = pd.merge(df1, df2, on="cliente_id")

# Mostra as primeiras linhas do resultado
print(dfMerged.head())

# Exporta para novo CSV
dfMerged.to_csv("merged_clientes_vendas.csv", index=False)


