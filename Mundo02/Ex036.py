# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
home = float(input("Digite o valor da casa que será adquirida: "))
salary = float(input("Qual o seu salário mensal? "))
years = int(input("Em quantos anos será o financiamento?"))
prestacao = home/(years*12)
print("Valor da Casa: R${:.2f}".format(home))
print("Período: {}".format(years))
print("Valor da Prestação: R${:.2f}".format(prestacao))

if prestacao>salary*0.3:
    print("Empréstimo negado, cada prestação será maior que 30% do seu salário")
else:
    print("Empréstimo aceito. Foi um prazer fazer negócios com você.")