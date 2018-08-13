'''
    Exercício 5.27 - Escreva um programa que verifique se um número é palíndromo.
    Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
    Exemplo: 454, 10501
'''
numero = input("Digite um número: ")

if numero == numero[::-1]:
    print("{} é um número palíndromo!".format(numero))
else:
    print("{} não é um número palíndromo!".format(numero))

