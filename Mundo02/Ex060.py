# Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input("Digite um número para calcular o fatorial: "))
aux = n
fat = 1
while aux > 0:
    fat = fat*aux
    aux -= 1
print("O fatorial de {} é {}".format(n, fat))
