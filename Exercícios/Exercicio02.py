# Receba ano de nascimento e ano atual. Calcule idade e semanas

# Entrada
anoNasc = int(input("Digite o ano de seu nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

#Processamento
idade = anoAtual - anoNasc
semanas = idade * 52

#Saída
print("Você viveu:")
print(f"{idade} anos")
print(f"{semanas} semanas")