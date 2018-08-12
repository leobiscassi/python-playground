'''
    Exercício 5.5 - Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
'''
x = 3
quantidade = 0

while quantidade + 1 <= 10:
    if x % 3 == 0:
        print(x)
        quantidade += 1
    x += 1

