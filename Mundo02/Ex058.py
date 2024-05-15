# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
import random
n = random.randint(0,10)
user = int(input("Tente advinhar o número que eu escolhi entre 0 e 10: "))
cont = 0
while user != n:
    user = int(input("Errou, tente novamente: "))
    cont += 1
print("Voce levou {} tentativas para acertar.".format(cont))
if cont == 0:
    print("Você é muito bom, parabéns!")
elif 1 <= cont <= 2:
    print("Foi um resultado bom")
elif 3 <= cont <= 7:
    print("Podia ter sido pior")
elif 8 <= cont <= 10:
    print("Não deve ser seu dia de sorte")
else:
    print("Como?")