# Receba a idade em anos e imprima em meses, dias, horas e minutos

# Entrada
idade = int(input("Digite sua idade: ")) # Pega o texto e converte em número

# Processamento
meses = idade * 12
dias = idade * 365
horas = dias * 24
minutos = horas * 60

# Saída
print("Você viveu:")
print(f"{idade} anos")
print(f"{meses} meses")
print(f"{dias} dias")
print(f"{horas} horas")
print(f"{minutos} minutos")