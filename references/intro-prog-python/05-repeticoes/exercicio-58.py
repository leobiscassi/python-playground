'''
    Exercício 5.8 - Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro
    pelo segundo. Utilize apenas os operadores de soma e substração para calcular o resultado. Lembre-se de que
    podemos entender a multiplicação de dois números como somas sucessivas de um deles.
    Assim: 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

x = 0
produto = 0

while x < n2:
    produto += n1
    x += 1

print("{} x {} = {}".format(n1, n2, produto))

