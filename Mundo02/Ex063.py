# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
# N primeiros elementos de uma Sequência de Fibonacci
n = int(input("Digite o número de termos da sequência de fibonacci: "))
t1 = 0
t2 = 1
while n != 0:
    print("{} -> ".format(t1), end='')
    aux = t2
    t2 += t1
    t1 = aux
    n -= 1
print("Fim")