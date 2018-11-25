'''
    Exercício 7.4 - Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa
    string.

    String: TTAAC
    Resultado:

    T: 2x
    A: 2x
    C: 1x
'''
string1 = input("Informe uma string: ")
l = []

for letra in string1:
    if letra not in l:
        print(f'{letra}: {string1.count(letra)}')
        l.append(letra)

