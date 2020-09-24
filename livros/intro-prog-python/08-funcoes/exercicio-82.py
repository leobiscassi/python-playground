'''
    Exercício 8.2 - Escreva uma função que receba dois números e retorne True se o primeiro número
    for múltiplo do segundo.

    Valores esperados:

    multiplo(8, 4) == True
    multiplo(7, 3) == False
    multiplo(5, 5) == True
'''
def multiplo(a, b):
    return a % b == 0

print(multiplo(8, 4))
print(multiplo(7, 3))
print(multiplo(5, 5))

