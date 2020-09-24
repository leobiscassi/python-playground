'''
    Exercício 4.8 - Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
    Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da
    operação solicitada.
'''
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Informe a operação que deseja realizar: ")
resultado = 0

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2

print("{} {} {} = {}".format(num1, operacao, num2, resultado))