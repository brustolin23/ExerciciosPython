# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print("Escolha o tipo de conversão: \n 1 - binário\n 2 - octal\n 3 - hexadecimal")
option = int(input())
number = int(input("Digite o número a ser convertido: "))
if option == 1:
    print("Convertido em binário: {}".format(bin(number)[2:]))
elif option==2:
    print("Convertido em Octal: {}".format(oct(number)[2:]))
elif option == 3:
    print("Convertido em hexadecimal: {}".format(hex(number)[2:]))
else:
    print("Você não selecionou uma opção válida. ")