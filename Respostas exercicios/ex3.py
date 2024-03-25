# a) Crie uma variável contendo uma frase e use o método split() para dividir a frase em uma lista de palavras. Em seguida, imprima cada palavra em uma linha separada.
frase = "O rato roeu a roupa do rei de Roma"
palavras = frase.split()
for palavra in palavras:
    print(palavra)

# b) Escreva uma função chamada inverter_string que receba uma string como parâmetro e retorne essa string invertida. Por exemplo, se a entrada for "python", a saída deve ser "nohtyp".
def inverter_string(texto):
    return texto[::-1]

# Testando a função inverter_string
print("String invertida de 'python':", inverter_string("python"))

# c) Escreva um programa que solicite ao usuário seu nome e imprima-o em letras maiúsculas e minúsculas.
nome = input("Digite seu nome: ")
print("Nome em letras maiúsculas:", nome.upper())
print("Nome em letras minúsculas:", nome.lower())

# d) Escreva um programa que conte o número de vogais em uma string inserida pelo usuário.
string = input("Digite uma string: ")
vogais = "aeiouAEIOU"
contagem = 0
for letra in string:
    if letra in vogais:
        contagem += 1
print("Número de vogais na string:", contagem)

# e) Escreva um programa que substitua todas as ocorrências de uma letra em uma string por outra letra. O usuário deve inserir a string original e as letras a serem substituídas.
string_original = input("Digite uma string: ")
letra_original = input("Digite a letra a ser substituída: ")
letra_substituta = input("Digite a letra substituta: ")
nova_string = string_original.replace(letra_original, letra_substituta)
print("Nova string após substituição:", nova_string)

# f) Escreva um programa que verifique se uma palavra inserida pelo usuário é um palíndromo (ou seja, se ela é a mesma quando lida da esquerda para a direita e vice-versa).
palavra = input("Digite uma palavra: ")
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
