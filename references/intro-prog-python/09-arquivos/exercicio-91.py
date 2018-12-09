'''
    Exercício 9.1 - Escreva um programa que receba o nome de um arquivo pela linha de comando
    e que imprima todas as linhas desse arquivo.
'''
import sys

arquivo = open(sys.argv[1], "r")

for linha in arquivo.readlines():
    print(linha)

arquivo.close()

