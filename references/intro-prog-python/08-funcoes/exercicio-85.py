'''
    Exercício 8.5 - Reescreva a função da listagem 8.5 de forma a utilizar os métodos de pesquisa
    em lista, visto no capítulo 7.

    Listagem 8.5

    def pesquise(lista, valor):
      for x, e in enumerate(lista):
        if e == valor:
          return x
      return None

    l = [10, 20, 25, 30]
    print(pesquise(l, 25)) #  2
    print(pesquise(l, 27)) #  None
'''
def pesquise(lista, valor):
    return lista.index(valor) if valor in lista else None


l = [10, 20, 25, 30]

print(pesquise(l, 25))
print(pesquise(l, 27))

