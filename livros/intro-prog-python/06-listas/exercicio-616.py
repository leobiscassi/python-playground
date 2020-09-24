'''
    Exercício 6.16 - Modifique o programa da listagem 6.44 para ordenar a lista em ordem
    decrescente. l = [1, 2, 3, 4, 5] deve ser ordenada como l = [5, 4, 3, 2, 1]
'''
l = [1, 2, 3, 4, 5]
fim = len(l)

while fim > 1:
    trocou = False
    x = 0

    while x < (fim - 1):
        if l[x] < l[x + 1]:
            trocou = True
            temp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = temp
        x += 1

    if not trocou:
        break
    fim -= 1

for e in l:
    print(e)

