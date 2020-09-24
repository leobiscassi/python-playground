'''
    Exercício 5.25 - Escreva um programa que calcule a raiz quadrada de um número.
    Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raíz quadrada,
    considere a base b = 2. Calcule p usando a fórmula p = (b + (n / b)) / 2. Agora, calcule o quadrado de p.
    A cada passo, faça b = p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre
    n e o quadrado de p for menor que 0.0001
'''
n = int(input("Digite o número a obter-se a raíz quadrada: "))
b = 2
p = 0
q = 0

while abs(round((n - q), 4)) >= 0.0001:
    p = (b + (n / b)) / 2
    q = p ** 2
    b = p

print("A raíz quadrada de {} é {}.".format(n, round(p, 2)))