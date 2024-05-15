# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
cont = 10
term = int(input("Informe o primeiro termo da Progressão Aritmética: "))
raz = int(input("Informe a razão da progressão: "))

while cont != 0:
    for c in range(0, cont):
        print("{} -> ".format(term), end='')
        term += raz
    print("...")
    cont = int(input("Quantos termos a mais você deseja exibir? "))