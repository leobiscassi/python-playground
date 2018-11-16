'''
    Exercício 6.13 - A lista de temperaturas de Mons, na Bélgica, foi armazenada nan lista
    T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a
    temperatura média.
'''
t = [-10, -8, 0, 1, 2, 5, -2, -4]

minimo = t[0]
maximo = t[0]
soma = 0

for e in t:
    if minimo > e:
        minimo = e

    if maximo < e:
        maximo = e

    soma += e

print("{} é a menor temperatura. {} é a maior temperatura. {} é a temperatura média.".format(minimo, maximo,
                                                                                             soma / len(t)))

