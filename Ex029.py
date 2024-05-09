# Esxreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80 Km/h mostre uma mensagem dizendo que ele foi multado
# A multa custará R$7,00 por Km acima do limite
distance = float(input("Digite a velocidade do carro analisado: "))
if distance>80:
    print("Que absurdo, esse carro deve ser multado!")
    multa = (distance - 80)*7
    print("O valor da multa será R${:.2f}".format(multa))
elif distance>=0:
    print("Esse condutor está seguindo as normas.")
else:
    print("O que isso significa? Ele está andando de ré?")
