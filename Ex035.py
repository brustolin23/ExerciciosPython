# Desencolca um programa que leia o comprimento de 3 retas e diga ao usuário se é possível formar
# um triângulo com elas

r1 = int(input("Digite o comprimento da primeira reta: "))
r2 = int(input("Digite o comprimento da segunda reta: "))
r3 = int(input("Digite o comprimento da terceira reta: "))
if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print("É possível formar um triângulo com essas retas")
else:
    print("Não é possível formar um triângulo com essas retas")

