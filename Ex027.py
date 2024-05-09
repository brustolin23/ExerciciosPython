# Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e último nome separadamente

name = input("Digite o nome completo: ")
print("Primeiro nome: {}".format(name.split()[0]))
print("Último nome: {}".format(name.split()[len(name.split())-1]))
