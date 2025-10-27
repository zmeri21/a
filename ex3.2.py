# -*- coding: utf-8 -*-
# Exercício 2 – Arrays (NumPy) e Series (Pandas) – sem filtragem
# Resolução completa com comentários que introduzem cada linha do código
# -----------------------------------------------------------------------------

# Importar a biblioteca NumPy para criar e manipular arrays numérico
import numpy as np

# Importar a biblioteca Pandas para criar e manipular Series (vetores rotulados)
import pandas as pd

# Criar um array NumPy com os números inteiros de 1 a 10 (inclusive)
meu_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Calcular a soma de todos os elementos do array
soma = sum(meu_array)
# Calcular a média (valor médio) dos elementos do array
media = np.mean(meu_array)
# Multiplicar todos os elementos do array por 2 (operação vetorial)
multiplicacao = meu_array * 2

# Criar uma lista de índices personalizados (letras de 'a' a 'j') para a Series
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Construir uma Series Pandas usando o array como dados e os índices personalizados
minha_serie = pd.Series(data=meu_array, index=lista)

# Mostrar o array original na consola
print(meu_array)
# Mostrar a soma calculada
print(soma)
# Mostrar a média calculada
print(media)
# Mostrar o resultado do array multiplicado por 2
print(multiplicacao)
# Mostrar a Series criada com índices personalizados
print(minha_serie)


# Usar um ciclo for para percorrer cada índice da Series e imprimir o par índice → valor
for data in minha_serie.index:
    valor = minha_serie[data]
    # Obter o valor associado ao índice atual
    
    # Imprimir o par índice → valor, demonstrando a iteração com for

