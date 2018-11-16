'''
    Exercício 6.12 - Altere o programa da listagem 6.33 de forma a imprimir o menor elemento da lista
'''
l = [1, 7, 2, 4]

minimo = l[0]

for e in l:
    if minimo > e:
        minimo = e

print(minimo)

