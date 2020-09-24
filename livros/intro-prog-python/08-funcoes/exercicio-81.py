'''
    Exercício 8.1 - Escreva uma função que retorne o maior de dois números.
    Valores esperados:

    maximo(5, 6) == 6
    maximo(2, 1) == 2
    maximo(7, 7) == 7
'''
def maximo(a, b):
    return a if ((a > b) and (b < a)) else b

print(maximo(5, 6))
print(maximo(2, 1))
print(maximo(7, 7))

