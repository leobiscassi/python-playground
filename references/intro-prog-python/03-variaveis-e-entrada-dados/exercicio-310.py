'''
    Exercício 3.10 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor
    do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
'''
salario = float(input("Informe o valor do salário: "))
perc = int(input("Informe o percentual de aumento: "))

print("O salário informado foi R$ {} e obteve {}% de aumento [R$ {}]; salário atual R$ {}.".format(salario, perc,
                                                        (salario * (perc/100)), (salario + (salario * (perc/100)))))
