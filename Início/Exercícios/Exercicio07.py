# Receba nome, cargo e salário e acrescente 10%

nome = input("Digite seu nome: ")
cargo = input("Digite seu cargo: ")
sal = float(input("Digite seu salário: "))

# Processamento
dez = (sal/100)*10
saln = sal + dez

# Saída
print(f"Seu novo salário é: {saln}")