# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
price = float(input("Digite o preço atual do produto: "))
newprice = price + (price * 0.05)
print("O novo valor do produto será R${}".format(round(newprice, 2)))
