'''
    Exercício 8.7 - Defina uma função recursiva que calcule o maior divisor comum (M.D.C.) entre dois
    números a e b, onde a > b
'''
def calcula_mdc(a, b):
    if b == 0:
        return a
    else:
        return calcula_mdc(b, a % b)

print(calcula_mdc(20, 24))
print(calcula_mdc(36, 90))

