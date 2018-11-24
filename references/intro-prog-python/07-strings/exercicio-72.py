'''
    Exercício 7.2 - Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns
    às duas strings lidas.

    1ª string: AAACTBF
    2ª string: CBT
    Resultado: CBT

    A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.
'''
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
l = []

for letra in string2:
    if (letra in string1) and not (letra in l):
        l.append(letra)

string3 = "".join(l)

print(f"{string3}")

