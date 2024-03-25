# a) Escreva um programa que solicite ao usuário um número e, em seguida, imprima se esse número é positivo, negativo ou zero.
numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# b) Escreva um programa que determine se um ano é bissexto ou não.
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

# c) Escreva um programa que solicite ao usuário uma nota de 0 a 100 e imprima se o aluno foi aprovado (nota maior ou igual a 60) ou reprovado.
nota = float(input("Digite a nota do aluno: "))
if nota >= 60:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")

# d) Escreva um programa que imprima os números de 1 a 10 usando um loop while.
numero = 1
while numero <= 10:
    print(numero)
    numero += 1

# e) Escreva um programa que calcule a soma dos números pares de 1 a 100.
soma = 0
numero = 2
while numero <= 100:
    soma += numero
    numero += 2
print("A soma dos números pares de 1 a 100 é:", soma)

# f) Escreva um programa que solicite ao usuário um número e imprima se esse número é primo ou não.
numero = int(input("Digite um número: "))
if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, "não é primo.")
            break
    else:
        print(numero, "é primo.")
else:
    print(numero, "não é primo.")
