# Faça um programa que receba o nome, cargo e salário de um funcionário. Se o
# funcionário ganhar abaixo de 1000 reais, calcule o salário acrescido de 10%. Ao final
# exiba o nome, o cargo e o salário desse funcionário

nome = input("Digite seu nome: ")
cargo = input("Digite seu cargo: ")
salario = float(input("Inofrme seu salário: "))

if salario < 1000:
    salario = salario + ((salario / 100) * 10)
    print(f"{nome}, seu novo salário é de R${salario:.2f}")
else:
    print(f"{nome}, seu salário continuará R${salario:.2f}")