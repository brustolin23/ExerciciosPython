# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
opc = 0
while opc != 5:
    print(''' [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa''')
    opc = int(input("Selecione uma opção "))
    if opc == 1:
        adc = n1 + n2
        print("O resultado da soma é {}".format(adc))
    elif opc == 2:
        mul = n1 * n2
        print("O resultado da multiplicação é {}".format(mul))
    elif opc == 3:
        if n1 > n2:
            print("O maior número é {}".format(n1))
        elif n2 > n1:
            print("O maior número é {}".format(n2))
        else:
            print("Não há maior número")
    elif opc == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif opc == 5:
        print("Obrigado por usar o programa")
    else:
        print("Opção inválida")
