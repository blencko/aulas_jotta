# 9. Orientação a Objetos:

# a) Crie uma classe chamada Pessoa com os atributos nome e idade. Escreva um método para imprimir os dados da pessoa.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)

# b) Crie uma classe chamada ContaBancaria com os atributos saldo e titular. Escreva métodos para depositar, sacar e imprimir o saldo.
class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def imprimir_saldo(self):
        print("Saldo:", self.saldo)

# c) Crie uma classe chamada Carro com os atributos marca, modelo e ano. Escreva métodos para acelerar, frear e imprimir os dados do carro.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print("Acelerando.")

    def frear(self):
        print("Freando.")

    def imprimir_dados(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)

# d) Crie uma classe chamada Círculo com o atributo raio. Escreva métodos para calcular a área e o perímetro do círculo.
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

# e) Crie uma classe chamada Animal com os atributos nome e idade. Escreva métodos para fazer o animal comer e dormir.
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def comer(self):
        print("O animal está comendo.")

    def dormir(self):
        print("O animal está dormindo.")

# f) Crie uma classe chamada Retângulo com os atributos comprimento e largura. Escreva métodos para calcular a área e o perímetro do retângulo.
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)