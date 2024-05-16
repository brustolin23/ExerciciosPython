# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print(f"{'='*5}Mercado dos Guri{'='*5}")
print("Aqui o preço é bem BAHixo tchê")
tot = 0
m1000 = 0
pbarato = 0
barato = ''
while True:
    print(f"{'='*20}")
    prod = str(input("Digite o nome do produto: "))
    while True:
        preco = float(input("Digite o preço do produto"))
        if preco > 0:
            break
    if tot == 0:
        pbarato = preco
        barato = prod
    tot += preco
    if pbarato > preco:
        pbarato = preco
        barato = prod
    if preco>=1000:
        m1000 +=1
    opc = str(input("Deseja continuar? (N para sair) ")).upper()
    if opc == 'N':
        break
print(f"O preço total é R${tot:.2f}")
print(f"Foram {m1000} produtos que custaram mais de R$1.000,00")
print(f"O produto mais barato é {barato} com o valor de R${pbarato:.2f}")