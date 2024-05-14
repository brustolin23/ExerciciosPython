#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

price = float(input("Informe o preço do produto: "))
print("Selecione o método de pagamento: \n 1 - Dinheiro\n 2 - Cartão")
opc = int(input())
if opc==1:
    desc = price - (price*0.1)
    print("O produto terá 10% de desconto e sairá por R${:.2f}".format(desc))
elif opc==2:
    print("Em quantas parcelas?")
    parc=int(input())
    if parc==1:
        desc = price - (price * 0.05)
        print("O produto terá 5% de desconto e sairá por R${:.2f}".format(desc))
    elif parc==2:
        print("O produto não terá desconto. Seu valor integral é: R${:.2f} e o valor da parcela é R${:.2f}".format(price, price/2))
    elif parc >=3:
        jur = price+(price*0.2)
        print("O produto terá juros de 20%. O valor total será R${:.2f} e cada parcela sairá por R${:.2f}".format(jur,jur/parc))
    else:
        print("Opção inválida")
else:
    print("Opção inválida")