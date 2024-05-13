#Faça umprograma que leia um ângulo e mostre na tela o valor de seu seno, cosseno e tangente
import math as m
ang = float(input("Informe o valor do ângulo: "))
rad = (ang*m.pi)/180
sen = m.sin(rad)
cos = m.cos(rad)
tg = m.tan(rad)
print("Seno: {:.4f}\nCosseno: {:.4f}\nTangente: {:.4f}".format(sen,cos,tg))
