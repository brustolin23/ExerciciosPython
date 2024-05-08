# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e mostrando o escolhido
import random as r
al1 = str(input("Digite o nome do primeiro aluno: "))
al2 = str(input("Digite o nome do segundo aluno: "))
al3 = str(input("Digite o nome do terceiro aluno: "))
al4 = str(input("Digite o nome do quarto aluno: "))

#É necessário utilizar lista, que fica entre colchetes
chamada = [al1, al2, al3, al4]

aux = r.randint(0, 3)
print("{} deve apagar o quadro.".format(chamada[aux]))
