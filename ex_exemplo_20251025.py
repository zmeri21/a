# -*- coding: utf-8 -*-
# =============================================================================
# EXERCÍCIO INTEGRADOR (1h15m) — Introdução à Programação + DataFrames Pandas + Seaborn
# =============================================================================
#
# Contexto:
#   Vais pôr em prática os tópicos das aulas:
#   - Python básico: comentários, variáveis, tipos, print(), input(), conversões (int, str, type, len)
#   - Estruturas de dados: list, tuple, set, dict
#   - NumPy: arrays e operações simples
#   - Pandas: importação CSV (read_csv), exploração (empty, head, tail, info, describe),
#             seleção ([ ], .loc[ ], .iloc[ ]), junção (merge), limpeza (astype/to_numeric,
#             str.replace, drop, dropna, fillna, duplicated/drop_duplicates, rename),
#             criação de colunas calculadas e exportação (to_csv)
#   - Visualização: gráfico simples com Seaborn (ex.: boxplot / countplot / regplot)
#
# Objetivo:
#   Em 90 minutos, construir um pequeno "pipeline" de dados sobre provas de ciclismo
#   (ou corrida) a partir de 3 CSVs (modelo relacional simples → DataFrame único "tidy"),
#   realizar limpeza/seleção, gerar estatísticas/visualizações e guardar um CSV final.
#
# Entregáveis:
#   1) src/solucao.py (código)
#   2) data/athletes.csv, data/races.csv, data/results.csv  (ou dados gerados por ti)
#   3) out/clean_results.csv
#   4) (opcional) out/plots/*.png
#
# Regras:
#   - Linguagem: Python 3.10+; podes usar: pandas, numpy, seaborn, matplotlib.
#   - Mantém o código legível (type hints e comentários quando útil).
#   - Trata erros previsíveis (inputs inválidos, ficheiros em falta, conversões).
#
# =============================================================================
# CENÁRIO E DADOS (pequeno "star schema" → DataFrame único)
# =============================================================================
#
# Tens 3 tabelas (CSV), com chaves "race_id" e "athlete_id":
#
#   data/athletes.csv
#     - athlete_id (PK), name, gender, age
#
#   data/races.csv
#     - race_id (PK), date (YYYY-MM-DD), distance_km, category
#
#   data/results.csv  (FACTOS)
#     - race_id (FK), athlete_id (FK), finish_time_min, avg_speed_kmh, notes
#
#
# =============================================================================
# TAREFAS (sugestão: copiar estas tarefas para o fundo, para seguir passo a passo)
# =============================================================================
#
# T0 — Arranque
#   - Criar estrutura de pastas:
#       .
#       ├─ src/
#       │   └─ solucao.py
#       ├─ data/   (CSV de entrada)
#       └─ out/    (CSV/plots de saída)
#
# T1 — Python básico + Estruturas
#   1. Usa input() para pedir o teu nome e idade. Converte idade para int e imprime
#      uma saudação formatada com f-string. (print, input, int, str, type, len)
#   2. Dado a lista [4,2,4,3,2], usa set para remover duplicados, volta a lista e ordena.
#      Cria um dict {n: n*n*n} para cada elemento único.
#   3. Cria um tuple com ('10K','MedioFundo') e demonstra a sua imutabilidade.
#
# T2 — NumPy + Series
#   4. Cria um array NumPy com números 1..10; calcula média, soma e multiplica por 2.
#   5. Converte o array numa Series do Pandas com índices ['a'..'j'].
#
# T3 — Importação & Exploração de DataFrames
#   6. Lê os 3 CSVs com pandas.read_csv (atenção ao path e separador).
#   7. Verifica df.empty, mostra 8 primeiras/últimas linhas (head/tail), df.info() e describe().
#   8. Garante tipos corretos:
#      - races.date → datetime (parse_dates no read_csv OU pd.to_datetime)
#      - results.avg_speed_kmh → remover vírgula decimal e converter para numérico
#      - results.finish_time_min → to_numeric(errors="coerce")
#
# T4 — Limpeza de dados
#   9. Remove linhas duplicadas em results (drop_duplicates).
#  10. Trata missing values:
#      - Para finish_time_min: decide uma estratégia (dropna OU fillna com mediana
#        por category, justificando em comentário).
#      - Para avg_speed_kmh: decide dropna/fillna quando necessário.
#  11. (Opcional) Corrige/renomeia rótulos de colunas para snake_case (rename/df.columns).
#
# T5 — Junção & Coluna Calculada
#  12. Junta os 3 DataFrames num único DataFrame "df" (pd.merge por race_id e athlete_id).
#  13. Cria a coluna calculada pace_min_per_km = finish_time_min / distance_km.
#  14. Gera estatísticas descritivas (describe, nunique por colunas-chave).
#
# T6 — Seleção & Filtros
#  15. Seleciona somente provas da category == '10K' com [] e máscara booleana.
#  16. Usa .loc para selecionar todas as atletas do género 'F' e colunas ['name','finish_time_min','pace_min_per_km'].
#  17. Usa .iloc para selecionar as 3 primeiras linhas e 3 primeiras colunas (demonstração).
#
# T7 — Exportação & Visualização
#  18. Exporta o DataFrame limpo para out/clean_results.csv (to_csv, index=False).
#  19. Cria pelo menos 1 gráfico Seaborn:
#      - Opção A (categórico): boxplot do finish_time_min por gender.
#      - Opção B (regressão): regplot de age vs finish_time_min (hue=gender, se quiseres via lmplot).
#      - Guarda como PNG na pasta out/plots.
#
# (T8 — Bónus, dificuldade extra)
#  20. Implementa flags via argparse (--drop-missing, --fill-missing=median/global).
#  21. Adiciona validações: impedir distance_km <= 0; sinalizar ages fora de [10, 90].
#
# =============================================================================
# REQUISITOS FUNCIONAIS
# =============================================================================
# RF1. Carregar 3 CSVs, inspecionar e garantir tipos coerentes.
# RF2. Limpar: lidar com vírgulas decimais, NaN, duplicados; renomear quando fizer sentido.
# RF3. Fundir tabelas e criar pelo menos 1 coluna calculada.
# RF4. Selecionar subconjuntos com [], .loc e .iloc (exemplos concretos).
# RF5. Exportar CSV final e produzir pelo menos 1 gráfico Seaborn.
#
# REQUISITOS NÃO FUNCIONAIS
# RNF1. Código modular/legível (funções pequenas, comentários claros).
# RNF2. Tratamento de erros com mensagens úteis (onde fizer sentido).
# RNF3. Reprodutibilidade (mesma entrada → mesma saída).
#
# =============================================================================
# PISTAS TÉCNICAS (resumop)
# =============================================================================
# - pd.read_csv('data/ficheiro.csv', parse_dates=['date'])            # importação
# - df.empty, df.head(8), df.tail(8), df.info(), df.describe()        # exploração
# - df['col'].str.replace(',', '.', regex=False)                      # limpar texto
# - pd.to_numeric(df['col'], errors='coerce')                         # coerção numérica
# - df.drop_duplicates(inplace=False)                                  # duplicados
# - df.dropna(...)  /  df.fillna(...)                                 # missing values
# - pd.merge(left=a, right=b, on='chave', how='inner')                 # junção
# - df['nova_col'] = df['a'] / df['b']                                # coluna calculada
# - df['col'].astype('bool')  /  df.rename(columns={'old':'new'})     # tipos/nomes
# - df.to_csv('out/clean_results.csv', index=False)                    # exportação
# - Seleção:
#     • df[df['category']=='10K']                                      # []
#     • df.loc[df['gender']=='M', ['finish_time_min','pace_min_per_km']]
#     • df.iloc[:3, :3]
# - Seaborn:
#     • sns.boxplot(x='gender', y='finish_time_min', data=df)
#     • sns.regplot(x='age', y='finish_time_min', data=df)  # ou sns.lmplot(..., hue='gender')
#
# =============================================================================
# CHECKLIST RÁPIDO
# =============================================================================
# [ ] Leste 3 CSVs? [ ] Tipos corretos? [ ] Limpeza (NaN/duplicados)?
# [ ] Merge feito? [ ] Coluna calculada criada?
# [ ] Seleções com [], .loc, .iloc demonstradas?
# [ ] CSV exportado sem índice? [ ] Plot Seaborn guardado?
#
# =============================================================================
# RELATÓRIO (no topo do teu src/solucao.py, máximo 10 linhas)
# =============================================================================
# - Explica decisões de limpeza (drop vs fillna, que valor escolheste e porquê)
# - Explica filtros/seleções e a métrica calculada
# - Aponta limitações e próximos passos (ex.: normalizar categorias, outliers)
#
# =============================================================================
# FIM DO ENUNCIADO — escreve o teu código por baixo deste bloco de comentários
# =============================================================================
