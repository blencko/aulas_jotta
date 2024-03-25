import unittest

# 12. Testes Unitários:

# a) Escreva um teste unitário para uma função simples que soma dois números.
def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(3, 4), 7)
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(-1, 1), 0)

# b) Escreva um teste unitário para uma função mais complexa que requer a manipulação de arquivos.
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

class TestLerArquivo(unittest.TestCase):
    def test_ler_arquivo(self):
        self.assertEqual(ler_arquivo('arquivo_teste.txt'), 'Conteúdo de teste.')

# c) Escreva um teste unitário para uma função que realiza cálculos matemáticos.
def multiplicacao(a, b):
    return a * b

class TestMultiplicacao(unittest.TestCase):
    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 4), 12)
        self.assertEqual(multiplicacao(0, 5), 0)
        self.assertEqual(multiplicacao(-2, 3), -6)

# d) Escreva um teste unitário para uma função que interage com um banco de dados.
# Suponha uma função que salva um usuário em um banco de dados.
def salvar_usuario(nome):
    # Código para salvar o usuário no banco de dados
    return True

class TestSalvarUsuario(unittest.TestCase):
    def test_salvar_usuario(self):
        self.assertTrue(salvar_usuario('Alice'))
        self.assertTrue(salvar_usuario('Bob'))

# e) Escreva um teste unitário para uma função que faz uma solicitação HTTP.
# Suponha uma função que faz uma solicitação GET para uma API.
import requests

def fazer_requisicao():
    resposta = requests.get('https://api.github.com')
    return resposta.status_code

class TestFazerRequisicao(unittest.TestCase):
    def test_fazer_requisicao(self):
        self.assertEqual(fazer_requisicao(), 200)

# f) Escreva um teste unitário para uma função que gera um resultado aleatório.
import random

def gerar_numero_aleatorio():
    return random.randint(1, 100)

class TestGerarNumeroAleatorio(unittest.TestCase):
    def test_gerar_numero_aleatorio(self):
        numero = gerar_numero_aleatorio()
        self.assertTrue(1 <= numero <= 100)

if __name__ == '__main__':
    unittest.main()