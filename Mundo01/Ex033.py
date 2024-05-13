# Faça um programa que leia 3 números e mostre qual é o maior e o menor
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
if n1 > n2 :
    if n2 > n3:
        print("O maior número é {} e o menor número é {}".format(n1, n3))
    elif n3 < n1:
        print("O maior número é {} e o menor número é {}".format(n1, n2))
    else:
        print("O maior número é {} e o menor número é {}".format(n3, n2))
elif n2 > n3:
    if n3 > n1:
        print("O maior número é {} e o menor número é {}".format(n2, n1))
    else:
        print("O maior número é {} e o menor número é {}".format(n2, n3))
else:
    print("O maior número é {} e o menor número é {}".format(n3, n1))