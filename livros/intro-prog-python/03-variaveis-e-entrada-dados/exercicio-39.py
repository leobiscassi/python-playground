'''
    Exercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
    Calcule o total em segundos.
'''
dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

segundos += ((((dias * 24) + horas) * 60) * 60)


print("O tempo total em segundos é {}s".format(segundos))