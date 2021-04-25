'''
    Exercício 8.14 - Altere o programa da listagem 7.45, o jogo da forca. Escolha a palavra
    a adivinhar utilizando números aleatórios.
'''
import random

palavras = ["casa", "bola", "mangueira", "uva", "quiabo", "computador",
            "cobra", "lentilha", "arroz"]

palavra = palavras[random.randint(0, len(palavras) - 1)]

for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""

    for letra in palavra:
        senha += letra if letra in acertos else "."

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou essa letra!")
        continue
    else:
        digitadas += tentativa

        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

    print("X==:==\nX  :  ")
    print("X  0  " if erros >= 1 else "X")

    linha2 = ""

    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "

    print("X%s" % linha2)
    linha3 = ""

    if erros == 5:
        linha3 += " /   "
    elif erros >= 6:
        linha3 += " / \ "

    print("X%s" % linha3)
    print("X\n=============")

    if erros == 6:
        print("Enforcado!")
        print("A palavra era '{0}'".format(palavra))
        break