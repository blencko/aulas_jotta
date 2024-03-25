def criar():
    for numero in range(1, 16):
        nome_arquivo = f'exercicio{numero}.py'  # Nome do arquivo
        with open(nome_arquivo, 'w') as arquivo:
            # Conteúdo inicial do arquivo
            conteudo = f'# Exercício {numero}\n\nif __name__ == "__main__":\n    pass\n'
            arquivo.write(conteudo)
        print(f'Arquivo {nome_arquivo} criado com sucesso.')

if __name__== "__main__":
    criar()