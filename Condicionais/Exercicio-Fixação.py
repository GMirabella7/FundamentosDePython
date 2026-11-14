# Solicite a temperatura ao usuário. Se estiver abaixo de 16 graus, informe ao usuário para pegar uma blusa. Ao final escreva fim do programa

temperatura = int(input("Digite a temperatura do ambiente em Celcius: "))

if temperatura <= 16:
    print("Está muito frio!🥶🥶🥶 Coloque uma blusa!!!")
else:
    print("Pegue um óculos de sol!!")

print("Fim do programa.")