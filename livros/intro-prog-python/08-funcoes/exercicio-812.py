'''
    Exercício 8.12 - Escreva uma função que receba uma string e uma lista. A função deve comparar
    a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro
    se a string for encontrada dentro da lista, e falso em caso contrário.
'''
string = "Biscassi"
lista1 = ["Léo", "Rodrigues", "Biscassi", "Silva"]
lista2 = ["Gabriel", "Tiago", "Olegário", "Marcus"]

def checa_string_lista(s, l):
    if s in l:
        return True
    else:
        return False

print(checa_string_lista(string, lista1))
print(checa_string_lista(string, lista2))

