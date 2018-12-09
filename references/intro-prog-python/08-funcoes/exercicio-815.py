'''
    Exercício 8.15 - Utilizando a função type, escreva uma função recursiva que imprima
    os elementos de uma lista. Cada elemento deve ser impresso separadamente, um por linha.
    Considere o caso de listas dentro de listas, como l = [1, [2, 3, 4, [5, 6, 7]]].
    A cada nível, imprima a lista mais à direita, como fazemos ao indexas blocos em python.
    Dica: envie o nível atual como parâmetro e utilize-o para calcular a quantidade de
    espaços em branco à esquerda de cada elemento.
'''
def imprime_lista(lista, c = 0):
    for e in lista:
        if type(e) == list:
            c += 1
            imprime_lista(e, c)
            c -= 1
        else:
            print((c * " ") + str(e))


l = [1, [2, 3, 4, [5, 6, 7]], [8, [9, 10]], 11]

imprime_lista(l)

