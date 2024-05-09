# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 para cada Km para viagens de até 200 Km
# e R$0,45 para viagens mais longas
distance = float(input("Digite a distância da viagem: "))
if 0 < distance <= 200:
    price = distance * 0.5
    print("A viagem custará R${:.2f}".format(price))
elif 200 < distance <= 12742:
    price = distance * 0.45
    print("A viagem custará R${:.2f}".format(price))
elif 12742 < distance:
    print("Não fazemos viagens para fora da terra")
else:
    print("Não inventamos viagens no tempo, ainda")
