'''
    Exercício 9.5 - Crie um programa que inverta a ordem das linhas do arquivo pares.txt
    A primeira linha deve conter o maior número; e a última, o menor.
'''
pares = open("pares.txt")
linhas = pares.readlines()
pares.close()
pares = open("pares.txt", "w")
pares.write("".join(linhas[::-1]))
pares.close()
