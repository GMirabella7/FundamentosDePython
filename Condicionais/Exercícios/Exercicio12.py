# Faça um programa que receba um número do usuário e informe se este número é par ou ímpar

num = int(input("Digite um número inteiro: "))
resto = num % 2

if resto == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é impar")