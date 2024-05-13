# Crie um programa que leia a frase informada pelo usuário e mostre:
# Quantas vezes aparece a letra 'A'
# Em qual posição se encontra o primeiro A
# Em qual posição se encontra o último A
phrase = input("Digite sua frase:\n")
print("A quantidade de 'A'(s) na frase é {}".format(phrase.upper().count('A')))
print("A primeira ocorrência foi na posição {}".format(phrase.upper().find("A")))
print("A última ocorrência foi na posição {}".format(phrase.upper().rfind("A")))
