'''
    Exercício 6.1 - Modifique o programa da listagem 6.6 para ler 7 notas em vez de 5.
'''
notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < len(notas):
    notas[x] = float(input("Nota %d: " % (x + 1)))
    soma += notas[x]
    x += 1

x = 0

while x < len(notas):
    print("Nota %d: %6.2f" % (x + 1, notas[x]))
    x += 1

print("Média: %5.2f" % (soma / x))