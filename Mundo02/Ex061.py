# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
cont = 0
term = int(input("Informe o primeiro termo da Progressão Aritmética: "))
raz = int(input("Informe a razão da progressão: "))

while cont < 10:
    print("{} -> ".format(term), end='')
    term += raz
    cont += 1
print("Fim")
