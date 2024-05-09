# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido. O programa deverá mostrar na tela se o usuário adivinhou ou não
import random
n = random.randint(0,5)
user = int(input("Tente advinhar o número que eu escolhi entre 0 e 5: "))
if n == user:
    print("Você conseguiu advinhar, parabéns")
else:
    print("Errado! Você realmente é ruim nisso!")
