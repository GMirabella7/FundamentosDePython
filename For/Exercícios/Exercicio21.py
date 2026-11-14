# Faça um programa que receba 15 números inteiros e imprima na tela a somatória dos 15 números

total = 0

for x in range(1, 16):
    num = int(input("Digite um número: "))
    total = total + num

print(f"Soma total: {total}")