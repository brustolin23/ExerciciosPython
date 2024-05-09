# Escreva um programa que leia um salário de um funcionário e calcule o valor do seu aumento.
# Para salários acima de R$1250,00 calcule um aumento de 10%
# Caso contrário, calcule um aumento de 15%
salary = float(input("Digite o valor do salário a ser reajustado: "))
if salary > 1250:
    newSalary = salary + (salary * 0.10)
else:
    newSalary = salary + (salary * 0.15)
print("O salário reajustado vale R${:.2f}".format(newSalary))
