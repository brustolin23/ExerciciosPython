#Crie um programa que leia um número real qualquer pelo teclado e mostre sua parte inteira
from math import trunc
real = float(input("Informe um número real: "))
#print("{:.0f}".format(real))
integer = trunc(real)
print("A parte inteira de {} é {}".format(real, integer))
