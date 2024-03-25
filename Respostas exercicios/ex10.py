# 10. Manipulação de Arquivos e Diretórios:

# a) Escreva um programa que leia o conteúdo de um arquivo JSON e imprima na tela.
import json

with open("arquivo.json", "r") as arquivo:
    conteudo = json.load(arquivo)
    print(conteudo)

# b) Escreva um programa que escreva um dicionário em um arquivo JSON.
dados = {"nome": "João", "idade": 30}

with open("arquivo.json", "w") as arquivo:
    json.dump(dados, arquivo)

# c) Escreva um programa que leia o conteúdo de um arquivo CSV e imprima na tela.
import csv

with open("arquivo.csv", "r") as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)

# d) Escreva um programa que escreva uma lista de listas em um arquivo CSV.
dados = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

with open("arquivo.csv", "w", newline="") as arquivo:
    escritor_csv = csv.writer(arquivo)
    for linha in dados:
        escritor_csv.writerow(linha)

# e) Escreva um programa que leia o conteúdo de um arquivo XML e imprima na tela.
import xml.etree.ElementTree as ET

tree = ET.parse("arquivo.xml")
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

# f) Escreva um programa que escreva uma lista de dicionários em um arquivo XML.
dados = [{"nome": "João", "idade": 30}, {"nome": "Maria", "idade": 25}]

root = ET.Element("pessoas")
for pessoa in dados:
    elem = ET.SubElement(root, "pessoa")
    for chave, valor in pessoa.items():
        sub_elem = ET.SubElement(elem, chave)
        sub_elem.text = str(valor)

tree = ET.ElementTree(root)
tree.write("arquivo.xml")