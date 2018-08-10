'''
    Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
    Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''
salario = float(input("Informe seu salário: "))
aumento = 0

if salario <= 1250:
    aumento = salario * 0.15
    salario += aumento
else:
    aumento = salario * 0.1
    salario += aumento

print("O aumento calculado foi R$ {}, o salário atual é R$ {}".format(aumento, salario))

