'''
    Exercício 6.11 - Modifique o programa da listagem 6.15 usando for. Explique por
    que nem todos os while podem ser transformados em for.
'''
l = []

# Este while não pode ser transformado em for porque a repetição é realizada por tempo indeterminado a priori
while True:
    n = int(input("Digite um número (0 sai): "))

    if n == 0:
        break

    l.append(n)

for i in l:
    print(i)

