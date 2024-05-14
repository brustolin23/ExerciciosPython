# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do
# homem mais velho e quantas mulheres têm menos de 20 anos.
sabio = ''
velho = 0
m20 = 0
for c in range(0,4):
    print("Pessoa {} ".format(c+1))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    genero = str(input("Gênero('m' ou 'f'):"))
    if genero.lower() == 'm' or genero.lower() == 'f':
        if genero.lower()=='m' :
            if idade > velho :
                velho = idade
                sabio = nome
        else:
            if idade >= 20:
                m20 += 1
    else:
        print("Gênero não reconhecido, cadastro anulado")
print("O homem mais velho é o senhor {} com seus {} anos".format(sabio,velho))
print("Foram cadastradas {} mulheres com mais de 20 anos".format(m20))
