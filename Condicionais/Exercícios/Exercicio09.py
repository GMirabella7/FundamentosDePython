# Uma empresa decide dar aumento de 30% aos funcionários cujo salário é inferior a
# 500 reais. Escreva um programa que receba o salário de um funcionário e imprima o
# valor do salário reajustado ou uma mensagem caso o funcionário não tenha direito a
# aumento

nome = input("Digite seu nome: ")
salario = float(input("Informe seu salário: "))

if salario < 500:
    salario = salario + ((salario / 100) * 30)
    print(f"Seu novo salário será de R${salario}")
else:
    print(f"Seu salário continuará R${salario}")