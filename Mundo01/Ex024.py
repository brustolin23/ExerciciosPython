# Crie um programa que leia o nome de uma cidade e informe se ela começa ou não com "Santo"
city = input("Digite o nome da cidade: ")
if "SANTO" in city.upper():
    if city.upper().find("SANTO") == 0:
        print("O nome da sua cidade começa com 'Santo'.")
    else:
        print("Sua cidade tem 'Santo' no nome mas não começa com ele")
else:
    print("Sua cidade não tem 'Santo'")