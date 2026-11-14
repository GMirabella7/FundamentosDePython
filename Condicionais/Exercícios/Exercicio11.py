# Faça um programa que receba um número inteiro do usuário e informe se este
# número é positivo ou negativo

num = int(input("Digite um número inteiro: "))

if num < 0:
    print(f"{num} é um número negativo")
elif num == 0:
    print(f"Seu número é 0")
else:
    print(f"{num} é um número positivo")