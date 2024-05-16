# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

midade = 0
h = 0
m20 = 0
while True:
    i = 0
    while i <= 0:
        i = int(input("Digite a Idade: "))
    while True:
        gen = str(input("Digite o genero: (M/F) ")).upper()
        if gen == 'M' or gen == 'F':
            break
    if i >= 18:
        midade += 1
    if gen == 'M':
        h += 1
    if gen == 'F' and i < 20:
        m20 += 1
    opc = str(input("Deseja continuar? (N para parar)")).upper()
    if opc == 'N':
        break
print(f"Foram cadastradas {midade} pessoas maiores de idade")
print(f"Foram {h} homens cadastrados e {m20} mulheres com menos de 20 anos")
