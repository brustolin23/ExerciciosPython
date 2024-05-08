# O mesmo professor do exercício 19 quer sortear a ordem de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random as r

al1 = str(input("Digite o nome do primeiro aluno: "))
al2 = str(input("Digite o nome do segundo aluno: "))
al3 = str(input("Digite o nome do terceiro aluno: "))
al4 = str(input("Digite o nome do quarto aluno: "))
chamada = [al1, al2, al3, al4]
r.shuffle(chamada)
print("1 - {}\n2 - {}\n3 - {}\n4 - {}".format(chamada[0],chamada[1],chamada[2],chamada[3]))
