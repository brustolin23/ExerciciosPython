# Crie um programa que leia o nome de uma pessoa e diga se ela tem ou não "Silva" nesse nome

name = input("Digite o nome desejado: ")
if "SILVA" in name.upper():
    print("Existe 'Silva' no nome informado")
else:
    print("Não tem 'Silva' no nome")