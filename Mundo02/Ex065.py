# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior
# e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
opc = ''
media = 0
cont = 0
maior = 0
menor = 0
while opc != 'N':
    n = int(input("Digite um número: "))
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
    media += n
    opc = str(input("Deseja continuar? (N - para parar)")).upper()
media = media/cont
print("Foram digitados {} números".format(cont))
print("A média entre eles é {}".format(media))
print("O maior número digitado foi {}".format(maior))
print("O menor número digitado foi {}".format(menor))
