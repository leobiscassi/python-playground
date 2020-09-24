'''
    Exercício 7.6 - Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira,
    dos caracteres da segunda pelos da terceira.

    1ª string: AATTCGAA
    2ª string: TG
    3ª string: AC

    Resultado: AAAACCAA
'''
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string3 = input("Digite a terceira string: ")

substituir = zip(list(string2), list(string3))
resultado = string1

for primeira, segunda in substituir:
    resultado = resultado.replace(primeira, segunda)

print(f"1ª string: {string1}")
print(f"2ª string: {string2}")
print(f"3ª string: {string3}")
print(f"Resultado: {resultado}")

