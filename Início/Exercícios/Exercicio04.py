# Receba nome, peso e altura. Calcule IMC

# Entrada
nome = input("Digite seu nome: ")
peso = float(input("Insira seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Processamento
imc = peso/(altura*altura)

# Saída
print(f"{nome}, seu IMC é: {imc:.2f}")