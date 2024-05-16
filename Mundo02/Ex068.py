# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random as rd
vit = 0
while True:
    print("Vamos jogar par ou ímpar.")
    n = 0
    while n not in range(1,11):
        n = int(input("Digite um número entre 1 e 10:\n"))
    while True:
        opc = str(input("Deseja par ou ímpar? (P/I)\n")).upper()
        if opc == 'P' or opc == 'I':
            break
    comp = rd.randint(1, 10)
    soma = n+comp
    if (soma % 2 == 0 and opc == 'I') or (soma % 2 == 1 and opc == 'P'):
        print("Você perdeu.")
        break
    vit += 1
    print("Novamente...")
print(f"Você ganhou {vit} vezes consecutivas")
