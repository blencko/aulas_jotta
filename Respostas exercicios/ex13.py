# 13. Conceitos Avançados:

# a) Escreva uma função que utilize lambda para calcular o quadrado de um número.
quadrado = lambda x: x ** 2

# Teste da função lambda
print(quadrado(5))  # Saída: 25

# b) Escreva uma função que utilize map para converter uma lista de strings em uma lista de inteiros.
strings_para_inteiros = lambda lista: list(map(int, lista))

# Teste da função map
lista_strings = ['1', '2', '3', '4', '5']
print(strings_para_inteiros(lista_strings))  # Saída: [1, 2, 3, 4, 5]

# c) Escreva uma função que utilize filter para filtrar números pares de uma lista.
filtrar_pares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))

# Teste da função filter
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtrar_pares(lista_numeros))  # Saída: [2, 4, 6, 8, 10]

# d) Escreva uma função que utilize reduce para calcular o produto de todos os elementos de uma lista.
from functools import reduce
produto_elementos = lambda lista: reduce(lambda x, y: x * y, lista)

# Teste da função reduce
lista_numeros = [1, 2, 3, 4, 5]
print(produto_elementos(lista_numeros))  # Saída: 120

# e) Escreva uma função que utilize decoradores para medir o tempo de execução de outra função.
import time

def medir_tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f'Tempo de execução de {funcao.__name__}: {fim - inicio} segundos')
        return resultado
    return wrapper

# Teste do decorador
@medir_tempo
def calcular_soma(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

print(calcular_soma(1000000))  # Saída: Tempo de execução de calcular_soma: 0.025003433227539062 segundos

# f) Escreva uma função que utilize geradores para gerar números de Fibonacci.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Teste do gerador
for numero in fibonacci(10):
    print(numero, end=' ')  # Saída: 0 1 1 2 3 5 8 13 21 34 