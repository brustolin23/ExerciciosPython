# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    t = int(input("Qual tabuada você quer ver? (use um número negativo para parar)\n"))
    if t < 0:
        break
    print(f"{'='*20}")
    for c in range(1,11):
        print(f"{t} X {c} = {c*t}")
    print(f"{'=' * 20}")
print("Obrigado por usar o programa!")