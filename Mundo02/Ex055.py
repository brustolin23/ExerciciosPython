# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = float(0)
menor = float(100000)
for c in range(0,5):
    peso = float(input("Digite o peso da pessoa {}\n".format(c+1)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("O menor peso é {:.2f}Kg".format(menor))
print("O maior peso é {:.2f}Kg".format(maior))
