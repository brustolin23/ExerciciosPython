# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao t0do sem considerar espaços
# Quantas letras tem o primeiro nome

name = input("Digite o nome completo: ")
print("Maiúsculas: {}".format(name.upper()))
print("Minúsculas: {}".format(name.lower()))
print("Quantidade total de letras? {}".format(len(name.replace(' ', ''))))
print("Quantas letras tem o primeiro nome? {}".format(len(name.split()[1])))
