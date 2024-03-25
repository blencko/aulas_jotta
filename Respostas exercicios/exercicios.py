# a) Declare duas variáveis, uma para armazenar seu nome e outra para armazenar sua idade. Em seguida, imprima essas variáveis na tela.
nome = "João"  # Declaração da variável nome
idade = 25     # Declaração da variável idade
print("Nome:", nome)   # Imprime o valor da variável nome
print("Idade:", idade) # Imprime o valor da variável idade

# b) Crie uma lista com três cores diferentes e imprima cada uma delas em uma linha separada.
cores = ["vermelho", "azul", "verde"]  # Criação da lista de cores
for cor in cores:   # Iteração sobre a lista de cores
    print(cor)      # Imprime cada cor

# c) Escreva um programa que solicite ao usuário seu nome e sua idade e imprima uma mensagem personalizada com essas informações.
nome = input("Digite seu nome: ")  # Solicita ao usuário que insira seu nome
idade = int(input("Digite sua idade: "))  # Solicita ao usuário que insira sua idade
print("Olá,", nome + "! Você tem", idade, "anos.")  # Imprime uma mensagem personalizada com o nome e a idade do usuário

# d) Escreva um programa que converta uma temperatura em Celsius para Fahrenheit. O usuário deve inserir a temperatura em Celsius.
celsius = float(input("Digite a temperatura em Celsius: "))  # Solicita ao usuário que insira a temperatura em Celsius
fahrenheit = (celsius * 9/5) + 32  # Converte a temperatura para Fahrenheit
print("Temperatura em Fahrenheit:", fahrenheit)  # Imprime a temperatura em Fahrenheit

# e) Escreva um programa que calcule e imprima a área de um círculo. O usuário deve inserir o raio do círculo.
import math  # Importa o módulo math para utilizar a constante pi
raio = float(input("Digite o raio do círculo: "))  # Solicita ao usuário que insira o raio do círculo
area = math.pi * (raio ** 2)  # Calcula a área do círculo
print("Área do círculo:", area)  # Imprime a área do círculo

# f) Escreva um programa que verifique se um número inserido pelo usuário é par ou ímpar e imprima o resultado.
numero = int(input("Digite um número: "))  # Solicita ao usuário que insira um número
if numero % 2 == 0:  # Verifica se o número é par
    print(numero, "é par.")  # Imprime uma mensagem informando que o número é par
else:
    print(numero, "é ímpar.")  # Imprime uma mensagem informando que o número é ímpar




