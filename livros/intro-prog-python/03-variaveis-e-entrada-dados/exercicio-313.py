'''
    Exercício 3.13 - Escreva um programa que converta uma temperatura digitada em ºC em ºF.
    A fórmula para essa conversão é: F = (9 * ºC) / 5 + 32
'''
celsius = int(input("Informe a temperatura em ºC: "))

print("{} ºC = {} ºF".format(celsius, ((9 * celsius) / 5 + 32)))

