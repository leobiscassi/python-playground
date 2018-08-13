'''
    Exercício 5.26 - Escreva um programa que calcule o resto da divisão inteira entre
    dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.
'''
dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))

quociente = 0
resto = 0

while dividendo > 0:
    if dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
    else:
        resto = dividendo
        dividendo = 0

print("Quociente {}, Resto {}".format(quociente, resto))

