# 8. Módulos e Pacotes:

# a) Escreva um programa que importe o módulo math e use suas funções para calcular a raiz quadrada de um número.
import math
numero = float(input("Digite um número: "))
print("Raiz quadrada:", math.sqrt(numero))

# b) Escreva um programa que importe um módulo criado por você mesmo e use uma função desse módulo.
import meu_modulo
print(meu_modulo.soma(3, 5))

# c) Escreva um programa que crie e importe um pacote próprio e use uma função desse pacote.
from meu_pacote import minha_funcao
print(minha_funcao())

# d) Escreva um programa que importe o módulo random e use suas funções para gerar um número aleatório entre 1 e 100.
import random
print("Número aleatório:", random.randint(1, 100))

# e) Escreva um programa que importe o módulo datetime e use suas funções para imprimir a data e hora atuais.
import datetime
print("Data e hora atuais:", datetime.datetime.now())

# f) Escreva um programa que importe o módulo os e use suas funções para obter o diretório de trabalho atual e alterá-lo.
import os
print("Diretório atual:", os.getcwd())
os.chdir("/caminho/novo")
print("Diretório alterado:", os.getcwd())
