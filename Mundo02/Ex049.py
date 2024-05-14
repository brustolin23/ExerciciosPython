# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
num = int(input('Digite o valor inteiro desejado: '))
print('{}Tabuada do {}{}'.format('='*5,num,'='*5))
for c in range(0,11):
    print('{} * {} = {}'.format(num, c, num*c))
