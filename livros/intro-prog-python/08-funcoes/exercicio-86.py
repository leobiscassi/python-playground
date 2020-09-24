'''
    Exercício 8.6 - Reescreva o programa da listagem 8.8 de forma a utilizar for em vez de while.

    Listagem 8.8

    def soma(l):
      total = 0
      x = 0
      while x < 5:
        total += l[x]
        x += 1
      return total

    l = [1, 7, 2, 9, 15]
    print(soma(l))
    print(soma([7, 9, 12, 3, 100, 20, 4]))
'''
def soma(l):
    total = 0

    for x in range(len(l)):
        total += l[x]

    return total

l = [1, 7, 2, 9, 15]
print(soma(l))
print(soma([7, 9, 12, 3, 100, 20, 4]))

