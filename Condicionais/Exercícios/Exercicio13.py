# Faça um programa que receba um número de usuário e exiba este número, apenas se for par

num = int(input("Digite um número inteiro: "))
resto = num % 2

if resto == 0:
    print(num)