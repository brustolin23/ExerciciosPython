# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


r1 = int(input("Digite o comprimento da primeira reta: "))
r2 = int(input("Digite o comprimento da segunda reta: "))
r3 = int(input("Digite o comprimento da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print("É possível formar um triângulo com essas retas")
    if r1 == r2 == r3:
        print("Será um triângulo Equilátero")
    elif r1 != r2 != r3 != r1:
        print("Será um triângulo Escaleno")
    else:
        print("Será um triângulo Isóceles")
else:
    print("Não é possível formar um triângulo com essas retas")

