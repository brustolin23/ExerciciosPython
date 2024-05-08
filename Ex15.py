# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
distance = float(input("Digite a quantidade de quilômetros que o carro alugado percorreu: "))
days = int(input("Digite a quantidade de dias que o carro alugado percorreu: "))
pricedist = distance * 0.15
priceday = days * 60
total = priceday + pricedist

print("O valor total é R${}, dividido em:".format(round(total, 2)))
print("R${} pela quantidade de quilômetros".format(round(pricedist, 2)))
print("R${} pela quantidade de dias".format(round(priceday, 2)))
