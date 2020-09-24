'''
    Exercício 7.8 - Modifique o jogo da forca de forma a utilizar uma lista de palavras.
    No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula:

    indice = (numero * 776) % len(lista_de_palavras)
'''

lista_de_palavras = []

while True:
    entrada = input("Digite uma palavra (0 para sair): ").lower().strip()

    if entrada == "0":
        break

    lista_de_palavras.append(entrada)

numero = int(input("\nDigite um número: "))
indice = (numero * 776) % len(lista_de_palavras)
palavra = lista_de_palavras[indice]

for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""

    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas.append(tentativa)

        if tentativa in palavra:
            acertos.append(tentativa)
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

