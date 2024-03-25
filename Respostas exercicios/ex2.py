# a) Escreva uma função chamada soma que receba dois números como parâmetros e retorne a soma deles.
def soma(a, b):
    return a + b

# Testando a função soma com dois números diferentes e imprimindo o resultado
print("Resultado da soma:", soma(5, 3))

# b) Escreva uma função chamada par_ou_impar que receba um número como parâmetro e retorne "Par" se o número for par ou "Ímpar" se for ímpar.
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Testando a função par_ou_impar com diferentes números
print("Número 4 é:", par_ou_impar(4))
print("Número 7 é:", par_ou_impar(7))

# c) Escreva uma função chamada maior_numero que receba uma lista de números como parâmetro e retorne o maior número da lista.
def maior_numero(lista):
    return max(lista)

# Testando a função maior_numero com uma lista de números
numeros = [10, 5, 8, 20, 15]
print("Maior número na lista é:", maior_numero(numeros))

# d) Escreva uma função chamada media que receba uma lista de números como parâmetro e retorne a média aritmética desses números.
def media(lista):
    return sum(lista) / len(lista)

# Testando a função media com uma lista de números
numeros = [10, 5, 8, 20, 15]
print("Média dos números na lista é:", media(numeros))

# e) Escreva uma função chamada inverte_lista que receba uma lista como parâmetro e retorne a lista invertida.
def inverte_lista(lista):
    return lista[::-1]

# Testando a função inverte_lista com uma lista
lista_original = [1, 2, 3, 4, 5]
print("Lista original:", lista_original)
print("Lista invertida:", inverte_lista(lista_original))

# f) Escreva uma função chamada conta_letras que receba uma string como parâmetro e retorne um dicionário onde as chaves são as letras da string e os valores são a quantidade de vezes que cada letra aparece na string.
def conta_letras(texto):
    dicionario = {}
    for letra in texto:
        if letra.isalpha():
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
    return dicionario

# Testando a função conta_letras com uma string
texto = "python programming"
print("Contagem de letras no texto:", conta_letras(texto))