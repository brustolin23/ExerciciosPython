# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retangulo e calcule e mostre o comprimento da hipotenusa.
import math as m
copo = float(input("Digite o valor do cateto oposto: "))
cadj = float(input("Digite o valor do cateto adjacente: "))
hip = m.sqrt(m.pow(cadj,2)+m.pow(copo,2))
print("O valor da hipotenusa é {:.2f}".format(hip))
