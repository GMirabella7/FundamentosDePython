# Receba nome, peso e altura. Calcule IMC

# Entrada
nome = input("Digite seu nome: ")
peso = float(input("Insira seu peso: "))
print(" kg")
altura = float(input("Digite sua altura: "))

# Processamento
imc = (altura*altura)/peso

# Saída
print(f"{nome}, seu IMC é: {imc}")