'''
    Exercício 9.2 - Modifique o programa do exercício 9.1 para que receba mais dois parâmetros: a linha de início e a
    de fim para impressão. O programa deve imprimir apenas as linhas entre esses dois valores (incluindo as linhas
    de início e fim).
'''
import sys

arquivo = open(sys.argv[1], "r")
inicio = int(sys.argv[2])
fim = int(sys.argv[3])


for i, linha in enumerate(arquivo.readlines()):
    if i >= inicio and i <= fim:
        print(linha)

