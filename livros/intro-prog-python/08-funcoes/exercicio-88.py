'''
    Exercício 8.8 - Usando a função mdc definida no exercício anterior, defina uma função para
    calcular o menor múltiplo comum (M.M.C.) entre dois números.
'''
def calcula_mdc(a, b):
    if b == 0:
        return a
    else:
        return calcula_mdc(b, a % b)

def calcula_mmc(a, b):
    return int(abs(a * b) / calcula_mdc(a, b))

print(calcula_mmc(4, 6))
print(calcula_mmc(7, 3))

