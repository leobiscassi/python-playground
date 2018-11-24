'''
    Exercício 7.3 - Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres
    que aparecem em uma delas.

    1ª string: CTA
    2ª string: ABC
    3ª string: BT

    A ordem dos caracteres da terceira string não é importante.
'''
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
l = []

for letra in string1:
    if letra not in string2:
        l.append(letra)

for letra in string2:
    if letra not in string1:
        l.append(letra)

string3 = "".join(l)

print(f"{string3}")

