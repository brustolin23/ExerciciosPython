# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
primo = True
num = int(input("Informe o número: "))
if num > 1:
    for c in range(2, num):
        if num % c == 0 and num != c:
            primo=False
else:
    primo = False
if primo:
    print("O número é primo")
else:
    print("O número não é primo")