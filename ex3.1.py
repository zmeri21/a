# -*- coding: utf-8 -*-
# Exercício 1 – Estruturas Nativas (Listas, Conjuntos, Dicionários)
# Resolução completa SEM definir funções, com comentários a introduzir cada linha do código
# -----------------------------------------------------------------------------

# Mostrar um título para indicar o objetivo do programa


# Definir uma lista de exemplo com elementos repetidos para o caso de não haver input do utilizador
minha_lista = [1, 2, 2, 1, 45, True]

# Mostrar a lista inicial (possivelmente com valores repetidos)
print(minha_lista)

# Converter a lista para um conjunto para remover automaticamente os duplicados
meu_conjunto = set(minha_lista)

# Apresentar o conjunto resultante para verificar a remoção de duplicados
print(meu_conjunto)

# Converter o conjunto de volta para uma lista para permitir ordenação
minha_lista_ordenada = list(meu_conjunto)

# Ordenar a lista de forma crescente para organizar os valores únicos
minha_lista_ordenada = sorted(minha_lista_ordenada)

# Mostrar a lista ordenada de elementos únicos
print(minha_lista_ordenada)

# Criar um dicionário vazio para mapear cada número ao seu quadrado
meu_dic = {}

# Percorrer cada número da lista ordenada utilizando um ciclo for
for num in minha_lista_ordenada:
    # Calcular o quadrado do número atual
   meu_dic[num] = num **2
    # Registar no dicionário a associação número → quadrado


# Apresentar o dicionário final que mapeia cada número ao seu quadrado
print(meu_dic)
