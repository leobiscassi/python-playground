'''
    Exercício 7.9 - Modifique o programa para utilizar listas de strings para desenhar o boneco da forca.
    Você pode utilizar ma lista para cada linha e organizá-las em uma lista de listas. Em vez de controlar
    quando imprimir cada parte, desenhe nessas listas, substituindo o elemento a desenhar.

    Exemplo:

    linha = list("X------")
    linha
     ['X', '-', '-', '-', '-', '-', '-']
    linha[6] = "|"
    linha
     ['X', '-', '-', '-', '-', '-', '|']
    "".join(linha)
     "X-----|"
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
linhas = []
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

    linha1 = list("X      ")
    linha2 = list("     ")
    linha3 = list("     ")

    linhas.append(linha1)
    linhas.append(linha2)
    linhas.append(linha3)

    if erros >= 1:
        linhas[0][3] = "0"

    print("X==:==\nX  :  ")
    print("".join(linhas[0]))

    if erros == 2:
        linhas[1][2] = "|"
    elif erros == 3:
        linhas[1][1] = "\\"
        linhas[1][2] = "|"
    elif erros >= 4:
        linhas[1][1] = "\\"
        linhas[1][2] = "|"
        linhas[1][3] = "/"

    print("X%s" % "".join(linhas[1]))

    if erros == 5:
        linhas[2][1] = "/"
    elif erros >= 6:
        linhas[2][1] = "/"
        linhas[2][3] = "\\"

    print("X%s" % "".join(linhas[2]))
    print("X\n=============")

    if erros == 6:
        print("Enforcado!")
        print("A palavra era '{0}'".format(palavra))
        break

