number1 = input('Digite um número: ')
if (number1.isnumeric()):
    number2 = input('Digite outro numero: ')
    if (number2.isnumeric()):
        soma = int(number1) + int(number2)
        print('O resultado da soma é: {}'.format(soma))
    else:
        print("Erro: o valor digitado não é um número.")
else:
    print("Erro: o valor digitado não é um número.")