# Operadores Lógicos
# AND - Ambas as experssões devem retornar verdadeiras (1)
# OR - Basta apenas uma das expressões retornar verdadeira (1)
# NOT - Inverte o resultado da expressão lógica

idade = int(input("Digite a sua idade: "))
ingresso = input("Você tem ingresso? (s/n) ")

# Conjugar com operador AND
if not(idade >= 18 and ingresso == "s") :
    print("Seja bem-vindo à festa 🎉🥳")
else:
    print("Você não pode entrar na festa 😡⚠️")