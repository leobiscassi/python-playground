'''
    Exercício 5.9 - Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo,
    assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado.
    Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos
    retirar o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

quociente = 0
resto = 0

while n1 > 0:
    if n1 >= n2:
        quociente += 1
        n1 -= n2
    else:
        resto = n1
        n1 = 0

print("Quociente {}, resto {}".format(quociente, resto))

