'''
    Exercício 8.4 - Escreva uma função que receba a base e a altura de um triângulo e
    retorne sua área (A = (base x altura) / 2).

    Valor esperado:

    area_triangulo(6, 9) == 27
    area_triangulo(5, 8) == 20
'''
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

print(area_triangulo(6, 9))
print(area_triangulo(5, 8))

