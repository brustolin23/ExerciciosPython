# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime as dt
menor = 0
maior = 0
today = dt.datetime.today().year
for c in range(0,7):
    ano = int(input("Digite o ano de nascimento da pessoa {}\n".format(c+1)))
    if today-ano >= 18:
        maior+=1
    else:
        menor+=1
print("Existem {} pessoas maiores de idade e {} menores de idade".format(maior,menor))