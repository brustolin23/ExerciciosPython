# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
s = float(input("Digite o salário atual: "))
news = s + (s * 0.15)
print("O novo salário será R${}".format(round(news, 2)))
