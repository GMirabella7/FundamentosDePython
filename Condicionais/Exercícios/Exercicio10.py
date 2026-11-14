# Elabore um programa para cálculo de preços de produtos que solicite o preço de
# compra do produto e o percentual a ser aplicado em cima desse valor para a venda.
# Calcule e exiba o preço de venda do produto. Se o percentual a ser aplicado for
# inferior a 50%, exiba uma mensagem informando ao usuário que o produto será
# vendido com uma margem muito pequena de lucro

precoCompra = float(input("Digite o valor de compra do produto: "))
percentualVenda = int(input("Digite o percentual de venda: "))

precoVenda = precoCompra + ((precoCompra / 100) * percentualVenda)

if percentualVenda < 0:
    print(f"O percentual de {percentualVenda}% dará prejuízo😭")
elif percentualVenda < 50:
    print(f"O percentual de {percentualVenda}% terá uma margem de lucro muito pequena😬")
else:
    print(f"O percentual de {percentualVenda}% está ótimo e dará muito lucro!🤑")

print(f"Você comprou o produto por R${precoCompra} e venderá por {precoVenda:.2f}")