'''
    Exercício 9.3 - Crie um programa que leia os arquivos pares.txt e impares.txt e que crie
    um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos, de forma a
    preservar a ordem númerica.
'''
pares = open("pares.txt")
impares = open("impares.txt")
paresimpares = open("pareseimpares.txt", "w")

pareseimpares = []

for l in pares.readlines():
    pareseimpares.append(int(l))

for l in impares.readlines():
    pareseimpares.append(int(l))

pareseimpares.sort()

for i in pareseimpares:
    paresimpares.write("{}\n".format(i))

pares.close()
impares.close()
paresimpares.close()

