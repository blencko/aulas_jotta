# 11. Documentação:

# a) Escreva um programa e adicione comentários explicativos para cada linha de código.
# Este é um exemplo simples de programa em Python que imprime "Olá, mundo!" na tela.
print("Olá, mundo!")

# b) Escreva uma função e adicione uma docstring explicando o propósito da função e seus parâmetros.
def saudacao(nome):
    """
    Esta função imprime uma saudação personalizada para o nome fornecido como argumento.

    Args:
        nome (str): O nome da pessoa para a qual a saudação será dirigida.
    """
    print("Olá,", nome, "! Bem-vindo!")

# c) Leia a documentação oficial de uma biblioteca Python de sua escolha e explique como você utilizaria essa biblioteca em um projeto.
# Por exemplo, se escolher a biblioteca requests, você pode usar o comando `pip install requests` para instalar.
# Em seguida, você pode importá-la em seus scripts Python usando `import requests` e utilizar suas funções para fazer solicitações HTTP.

# d) Escreva um programa que utilize uma biblioteca externa e adicione comentários explicativos sobre como essa biblioteca está sendo usada.
# Por exemplo, se estiver usando a biblioteca numpy para cálculos matemáticos, você pode importá-la usando `import numpy as np` e, em seguida, usar funções como `np.array()` para criar arrays e realizar operações matemáticas.

# e) Crie um documento README.md para um projeto pessoal e inclua instruções de instalação, uso e exemplos.
# O README.md deve conter informações sobre como instalar o projeto, como utilizá-lo e exemplos de código ou exemplos de aplicação.

# f) Escreva uma função e adicione comentários explicando os possíveis erros que podem ocorrer durante a execução da função e como eles podem ser tratados.
def dividir(a, b):
    """
    Esta função divide dois números e retorna o resultado.
    
    Args:
        a (int/float): O dividendo.
        b (int/float): O divisor.
        
    Returns:
        float: O resultado da divisão.
        
    Raises:
        ZeroDivisionError: Se o divisor for zero.
    """
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
        return None