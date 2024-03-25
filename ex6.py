# 6. Funções:

# a) Escreva uma função chamada soma_intervalo que receba dois números como parâmetros e retorne a soma de todos os números inteiros no intervalo entre esses dois números (inclusive).
def soma_intervalo(a, b):
    return sum(range(a, b + 1))

# b) Escreva uma função chamada fatorial que receba um número como parâmetro e retorne o fatorial desse número.
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# c) Escreva uma função chamada verifica_primo que receba um número como parâmetro e retorne True se o número for primo e False caso contrário.
def verifica_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# d) Escreva uma função chamada media_lista que receba uma lista de números como parâmetro e retorne a média aritmética desses números.
def media_lista(lista):
    return sum(lista) / len(lista)

# e) Escreva uma função chamada maior_string que receba uma lista de strings como parâmetro e retorne a maior string dessa lista.
def maior_string(lista):
    return max(lista, key=len)

# f) Escreva uma função chamada quantidade_vogais que receba uma string como parâmetro e retorne a quantidade de vogais (a, e, i, o, u) nessa string.
def quantidade_vogais(string):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in string if letra in vogais)