
# 7. Manipulação de Arquivos e Diretórios:
# a) Escreva um programa que leia o conteúdo de um arquivo de texto e imprima na tela.
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)

# b) Escreva um programa que conte o número de linhas em um arquivo de texto.
with open("arquivo.txt", "r") as arquivo:
    num_linhas = sum(1 for linha in arquivo)
print("Número de linhas:", num_linhas)

# c) Escreva um programa que copie o conteúdo de um arquivo para outro arquivo.
with open("arquivo_origem.txt", "r") as origem:
    conteudo = origem.read()
    with open("arquivo_destino.txt", "w") as destino:
        destino.write(conteudo)

# d) Escreva um programa que verifique se um arquivo de texto existe em um determinado diretório.
import os
caminho = "/caminho/para/seu/arquivo.txt"
if os.path.exists(caminho):
    print("O arquivo existe.")
else:
    print("O arquivo não existe.")

# e) Escreva um programa que crie um diretório com um nome especificado pelo usuário.
nome_diretorio = input("Digite o nome do diretório: ")
os.makedirs(nome_diretorio)

# f) Escreva um programa que liste todos os arquivos em um diretório especificado pelo usuário.
caminho = input("Digite o caminho do diretório: ")
arquivos = os.listdir(caminho)
print("Arquivos no diretório:")
for arquivo in arquivos:
    print(arquivo)
