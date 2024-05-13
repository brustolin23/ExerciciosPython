# Escreva um programa que converta uma temperatura digitada em graus celcius para Fahrenheit
c = float(input("Digite a temperatura em graus celcius: "))
f = (c * 9) / 5 + 32
print("A temperatura em farenheit é {} grau(s)".format(round(f, 2)))
