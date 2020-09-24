'''
    Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.
'''
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = 0
menor = 0

#  Número 1 é maior que Número 2? Número 1 é maior que Número 3? Maior número = Número 1
#  Número 2 é maior que Número 1? Número 2 é maior que Número 3? Maior número = Número 2
#  Número 3 é maior que Número 1? Número 3 é maior que Número 2? Maior número = Número 3
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num1:
    menor = num3

print("O maior número é {}, e o menor número é {}.".format(maior, menor))

