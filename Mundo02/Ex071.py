# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print(f"{'='*20}")
print(f"Caixa dos Guri")
print(f"{'='*20}")
valor = int(input("Qual o valor do saque? "))
n50 = n20 = n10 = n1 = 0
while True:
    if valor >= 50:
        valor -= 50
        n50 += 1
    elif valor >= 20:
        valor -= 20
        n20 += 1
    elif valor >= 10:
        valor -= 10
        n10 += 1
    elif valor >= 1:
        valor -= 1
        n1 += 1
    else:
        break
print(f"{'='*20}")
if n50!=0:
    print(f"Serão {n50} notas de 50")
if n20!=0:
    print(f"Serão {n20} notas de 20")
if n10!=0:
    print(f"Serão {n10} notas de 10")
if n1!=0:
    print(f"Serão {n1} notas de 1")
print(f"{'=' * 20}")
print("Obrigado pela preferência")
