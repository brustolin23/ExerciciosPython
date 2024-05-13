# Exercício Python 041: A Confederação Nacional de Natação
# precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
import datetime as dt
today = dt.datetime.today().year
year = int(input("Digite o ano de nascimento do atleta: "))
age = today - year
if age <= 9:
    print("Categoria Mirim")
elif 14 >= age > 9:
    print("Categoria Infantil")
elif 19 >= age > 14:
    print("Categoria Júnior")
elif 25 >= age > 19:
    print("Categoria Sênior")
elif age > 25:
    print("Categoria Mestre")
