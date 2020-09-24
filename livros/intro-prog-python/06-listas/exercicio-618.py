'''
    Exercício 6.18 - Escreva um programa que gere um dicionário, onde cada chave seja um caractere, e seu valor
    seja o número desse caractere encontrado em uma frase lida.

    Exemplo: O rato -> {"O" : 1, "r" : 1, "a" : 1, "t" : 1, "o" : 1}
'''
frase = input("Digite uma frase: ")
frase = frase.strip().replace(" ", "")

dicionario = {}

for letra in frase:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

print(dicionario)

