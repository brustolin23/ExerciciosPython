# Faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta
# necessária para pintá-la, considerando que cada litro de tinta pinta 2 metros quadrados.

l = float(input("Digite a largura da parede a ser pintada: "))
a = float(input("Digite a altura da parede a ser pintada: "))

area = l * a
ink = area/2
print("A área total da parede é de {}".format(area))
print("A quantidade de tinta necessária para pintar essa área é {} litros".format(ink))
