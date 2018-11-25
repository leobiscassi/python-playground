'''
    Exercício 7.5 - Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres
    da segunda foram retirados da primeira.

    1ª string: AATTGGAA
    2ª string: TG
    3ª string: AAAA
'''
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string3 = []

for letra in string1:
    if letra not in string2:
        string3.append(letra)

print(f"1ª string: {string1}")
print(f"2ª string: {string2}")
print(f"3ª string: {''.join(string3)}")

