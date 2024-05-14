# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input("Digite uma frase\n"))
frase = frase.replace(" ", "")
#reverse = frase[::-1]
reverse = ''
for c in range(len(frase)-1,-1,-1):
    reverse+=frase[c]
if frase.lower() == reverse.lower():
    print("É palíndromo")
else:
    print("Não é palíndromo")

