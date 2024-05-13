# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# Desafio: Faça a validação se é homem ou mulher
import datetime as dt
gender = input("Você é homem ou mulher? \n m - mulher\n h - homem")
if gender=='f':
    print("Você não precisa fazer alistamento obrigatório")
elif gender=='m':
    year = int(input("Digite seu ano de nascimento: "))
    today = dt.datetime.today().year
    age = today - year
    if 0 <= age < 18:
        print("Você ainda não precisa se alistar, falta {} ano(s). Seu alistamento será em {}".format((18-age), (year+18)))
    elif age == 18:
        print("Você precisa se alistar esse ano!")
    elif age > 18:
        print("Você já perdeu o prazo! São {} ano(s) de atraso!! Voce deveria ter se alistado em {}!!!".format((age-18), (year+18)))
    else:
        print("Você veio do futuro?")
else:
    print("Eu não sei se você precisa se alistar")