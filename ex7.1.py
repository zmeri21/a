# ============================================================
# Biblioteca Pública — DataFrames, Seleção, Limpeza & Seaborn (1h)
# INSTRUÇÕES:
# 1) Acrescenta o codigo em falta.
# 2) Adiciona COMENTÁRIOS de linha (# ...) que:
#    - Respondam às perguntas Q1..Q9 onde indicado (escreve as respostas como comentários).
# 3) Entrega este .py com os teus comentários.
# ============================================================


# -----------------------------
# Dataset embutido (DICIONÁRIO)
# Contexto: Empréstimos de livros por leitores de uma Biblioteca
# -----------------------------
data = {
    "patron": [
        "Ana", "Bruno", "Carla", "Diogo", "Eva", "Filipe",
        "Goncalo", "Helena", "Ines", "Joao", "Joao", "Marisa"
    ],
    "age": [24, 31, 28, 35, 22, 29, 40, 27, 24, 31, 31, 33],
    "gender": ["F", "M", "F", "M", "F", "M", "M", "F", "F", "M", "M", "F"],
    # valores "sujos": None (missing) e "5h" (string com sufixo)
    "weekly_reading_hours": [6, 4, None, 5, 3, 4, 5, 4, 6, 4, 4, "5h"],
    "loan_duration_days": [12.0, 15.0, 14.0, 21.0, 18.0, 16.0, 25.0, 13.0, 12.0, 15.0, 15.0, 17.0],
    "branch": ["Central", "Central", "Riverside", "Norte", "Central", "Riverside", "Norte", "Central", "Central", "Central", "Central", "Riverside"],
    "city": ["Coimbra", "Coimbra", "Porto", "Lisboa", "Coimbra", "Porto", "Lisboa", "Coimbra", "Coimbra", "Coimbra", "Coimbra", "Porto"],
}

# ============================================================
# 1) LOAD
# ============================================================
import pandas as pd
import numpy as np
df = pd.DataFrame(data)
# Q1: Quantas linhas e colunas tem o dataset original? (Responde aqui em comentário.)
print(df.shape)
# ============================================================
# 2) LIMPEZA BÁSICA
# - 'weekly_reading_hours' tem um valor sujo '5h'. Converte para numérico.
# - Valores que não consigam ser convertidos ficam como NaN.
# ============================================================
df['weekly_reading_hours'] = df['weekly_reading_hours'].replace('5h', '5')
df['weekly_reading_hours'] = pd.to_numeric(df['weekly_reading_hours'], errors= "coerce")

# Q2: Quantos NaN existem agora em 'weekly_reading_hours'? (Responde aqui.)
print(df['weekly_reading_hours'].isna().sum())

# Q3: Indica UMA razão para manter NaN (em vez de apagar logo as linhas). (Responde aqui.)
#R: Manter os valores NaN permite analisar onde existem dados em falta
# ============================================================
# 3) NOVA COLUNA
# - 'days_per_hour' = loan_duration_days / weekly_reading_hours
#   (medida ilustrativa; NaN pode propagar)
# ============================================================
df['days_per_hour'] = df.loan_duration_days/ df.weekly_reading_hours
print(df['days_per_hour'])

# Q4: Para a leitora 'Ana', qual o valor de 'days_per_hour'? (Escreve o número que vês.)
filtro = (df["patron"]== "Ana")
df_ana = df[filtro]
total_ana = df_ana['days_per_hour'].sum()
print(total_ana)
# ============================================================
# 4) REMOVER DUPLICADOS (linhas duplicadas exatamente iguais)
#    Dica: há uma linha duplicada de 'Joao'.
# ============================================================
print("antes", df)
df = df.drop_duplicates()
print("depois", df)

# Q5: Quantas linhas duplicadas foram removidas? (Responde aqui.)
#R: 1
# ============================================================
# 5) FILTRAGEM (seleção com máscaras booleanas)
# - Mantém leitores com >= 4 horas/semana E empréstimos < 20 dias.
# ============================================================
filtro = (df["weekly_reading_hours"]>= 4) & (df["loan_duration_days"]< 20)
print(df.patron[filtro])
# Q6: Quantas linhas ficam após este filtro? (Responde aqui.)
print(len(df[filtro]))
# Q7: Quem tem o empréstimo mais curto (mínimo 'loan_duration_days') no conjunto filtrado?
#     (Se houver empate, lista os nomes empatados.) (Responde aqui.)
filtro2 = df.loan_duration_days[filtro].min()
print(filtro2)
df_min = df[filtro][df["loan_duration_days"][filtro] == filtro2]
print(df_min["patron"])

# ============================================================
# 6) SELEÇÃO: [], .loc e .iloc
#    Explica em comentários as diferenças e o que cada linha seleciona.
# ============================================================

# 6a) Usando [] para selecionar duas COLUNAS (devolve DataFrame)
sub_df_cols = df[["patron", "city"]]
print(sub_df_cols)

# 6b) Usando .loc com ETIQUETAS (labels) para linhas e colunas (devolve dataframe 2x2)
sub_df_loc = df.loc[0:1, ["patron","city"]]
print(sub_df_loc)

# 6c) Usando .iloc com POSIÇÕES inteiras para linhas/colunas (devolve dataframe 2x2)
sub_df_iloc = df.iloc[:2, [1, 2]]
print(sub_df_iloc)

# (Aqui: explica em comentários as diferenças chave entre [], .loc e .iloc no exemplo citado)

# ============================================================
# 7) LIMPEZA — TRATAR MISSING VALUES
# - Cria df_clean removendo linhas com NaN em 'weekly_reading_hours' OU 'loan_duration_days'.
# - Refaz o mesmo filtro do ponto 5 e compara os resultados com os anteriores.
# ============================================================
filtro_com_nan = df['weekly_reading_hours'].isna() | df['loan_duration_days'].isna()
df_clean = df.drop(df[filtro_com_nan].index)
print(df_clean)
filtro_original = (df_clean["weekly_reading_hours"] >= 4) & (df_clean["loan_duration_days"] < 20)
df_clean_filtrado = df_clean[filtro_original]
# Q8: O número de linhas no conjunto filtrado mudou após remover NaN?
#     Diz o valor antes e depois e explica porquê (em 1–2 frases). (Responde aqui.)
print(f"Linhas filtradas (original): {len(df_clean_filtrado)}")
print(f"Linhas filtradas (limpo): {len(df_clean)}")
# ============================================================
# 8) SEABORN
# - Visualiza, com um gráfico simples, quantos registos filtrados existem por 'branch'.
# - Observa o gráfico e responde à pergunta.
# ============================================================
import seaborn as sns
import matplotlib.pyplot as plt

# Gráfico de contagem por 'branch' no DataFrame filtrado e limpo
sns.countplot(data=df_clean_filtrado, x='branch')
# Título do gráfico (opcional)
plt.title("Leitores filtrados por branch")
# Mostrar gráfico
plt.show()




# Q9: Pelo gráfico, qual é a filial (branch) com MAIOR número de registos no conjunto limpo e filtrado?
#     (Se houver empate, indica as filiais empatadas.) (Responde aqui.)


# ============================================================
# FIM — A avaliação considera a clareza e correção dos teus comentários.
# ============================================================
