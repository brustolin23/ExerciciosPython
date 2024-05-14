# Crie um programa que faça o computador jogar Jokenpô com você.
import random as rd
player = int(input("Selecione uma opção para jogar:\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\n"))
computer = rd.randint(1, 3)
if (computer==1):
    print("O computador jogou Pedra")
elif (computer==2):
    print("O computador jogou Papel")
else:
    print("O computador jogou Tesoura")
if computer==player:
    print("Vocês empataram")
elif (player==1 and computer==2)or(player==2 and computer==3)or(player==3 and computer==1):
    print("Você perdeu")
elif (player==2 and computer==1)or(player==3 and computer==2)or(player==1 and computer==3):
    print("Você ganhou, parabéns!!")
else:
    print("Você selecionou uma opção inválida")
