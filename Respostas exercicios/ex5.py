# a) Escreva um programa que gere uma lista dos quadrados dos números de 1 a 10 usando uma compreensão de lista.
quadrados = [numero ** 2 for numero in range(1, 11)]
print("Quadrados dos números de 1 a 10:", quadrados)

# b) Escreva um programa que gere uma lista contendo apenas os números pares de 1 a 20 usando uma compreensão de lista.
pares = [numero for numero in range(1, 21) if numero % 2 == 0]
print("Números pares de 1 a 20:", pares)

# c) Escreva um programa que gere uma lista dos cubos dos números pares de 1 a 10 usando uma compreensão de lista.
cubos_pares = [numero ** 3 for numero in range(1, 11) if numero % 2 == 0]
print("Cubos dos números pares de 1 a 10:", cubos_pares)

# d) Escreva um programa que gere uma lista contendo o quadrado dos números ímpares de 1 a 15 usando uma compreensão de lista.
quadrados_impares = [numero ** 2 for numero in range(1, 16) if numero % 2 != 0]
print("Quadrados dos números ímpares de 1 a 15:", quadrados_impares)

# e) Escreva um programa que gere uma lista dos números de 1 a 1000 que são divisíveis por 7 usando uma compreensão de lista.
divisiveis_por_7 = [numero for numero in range(1, 1001) if numero % 7 == 0]
print("Números divisíveis por 7 de 1 a 1000:", divisiveis_por_7)

# f) Escreva um programa que gere uma lista contendo o dobro dos números impares de 1 a 20 usando uma compreensão de lista.
dobro_impares = [numero * 2 for numero in range(1, 21) if numero % 2 != 0]
print("Dobro dos números ímpares de 1 a 20:", dobro_impares)
