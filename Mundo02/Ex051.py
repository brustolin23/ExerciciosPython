# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

term = int(input("Informe o primeiro termo da Progressão Aritmética: "))
raz = int(input("Informe a razão da progressão: "))

for c in range(0,10):
    print("{} -> ".format(term), end='')
    term += raz
print("Fim")
