# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
soma = 0
for c in range(3,501,3):
    if (c%2==1):
        soma+=c
print("A soma de todos os múltiplos de 3 entre 3 e 500 é {}".format(soma))
