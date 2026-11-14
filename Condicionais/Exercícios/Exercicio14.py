# Faça um programa receba dois valores e imprima qual é o maior número digitado

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
else:
    print(f"O número {num2} é maior que o número {num1}")