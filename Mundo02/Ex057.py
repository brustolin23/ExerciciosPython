# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
gen = str(input("Digite seu gênero(M ou F): \n")).upper()
while gen !='M' or gen != 'F':
    gen = input("Genero não reconhecido, digite novamente: \n").upper()
if gen =='M':
    print("Gênero informado: Masculino")
else:
    print("Gênero informado: Feminino")
