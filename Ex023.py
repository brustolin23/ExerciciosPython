# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada dígito separado em
# unidade, dezena, centena e milhar

num = input("Digite um número de 0 a 9999: ")
if num.isnumeric():
    if len(num)<=4:
        print("Unidade: {}".format(num[3]))
        print("Dezena: {}".format(num[2]))
        print("Centena: {}".format(num[1]))
        print("Milhar: {}".format(num[0]))
    else:
        print("O número ultrapassou o limite")
else:
    print("O valor digitado deve ser um número")
