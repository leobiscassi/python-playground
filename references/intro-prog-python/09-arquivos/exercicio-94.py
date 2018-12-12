'''
    Exercício 9.4 - Crie um programa que receba o nome de dois arquivos como parâmetros de linha de comando
    e que gere um arquivo de saída com as linhas do primeiro e do segundo arquivo.
'''
import sys

primeiro_caminho = sys.argv[1]
segundo_caminho = sys.argv[2]

arquivo1 = open(primeiro_caminho)
arquivo2 = open(segundo_caminho)
arquivo3 = open("arquivo3.txt", "w")

conteudo1 = arquivo1.readlines()
conteudo2 = arquivo2.readlines()
conteudo3 = conteudo1 + conteudo2

arquivo3.write("".join(conteudo3))

arquivo1.close()
arquivo2.close()
arquivo3.close()

