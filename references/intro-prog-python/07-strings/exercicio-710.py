'''
    Exercício 7.10 - Escreva um jogo da velha para dois jogadores. O jogo deve perguntar
    onde você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
    posição está livre. Verifique também quando um jogador venceu a partida. Um
    jogo da velha pode ser visto como uma lista de 3 elementos, onde cada elemento é outra
    lista, também com três elementos.

    Exemplo do jogo:

    X | 0 |
   ---+---+---
      | X | X
   ---+---+---
      |   | 0


    Onde cada posição pode ser vista como um número. Confira abaixo um exemplo das posições mapeadas para a mesma
    posição de seu teclado numérico.

    7 | 8 | 9
   ---+---+---
    4 | 5 | 6
   ---+---+---
    1 | 2 | 3
'''
mensagem = '''
    7 | 8 | 9
   ---+---+---
    4 | 5 | 6
   ---+---+---
    1 | 2 | 3 \n\n'''

print("\n\nMAPA DO TABULEIRO\n")
print(mensagem)
print("Para jogar cada jogador deve informar o número da posição desejada.")

simbolos = {1 : "X", 2 : "0"}

mapa = {1 : (2, 0), 2 : (2, 1), 3 : (2, 2),
        4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
        7 : (0, 0), 8 : (0, 1), 9 : (0, 2)}

combinacoes = [((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 1), (2, 1)),
               ((0, 2), (1, 2), (2, 2)),
               ((0, 2), (1, 1), (2, 0)),
               ((0, 0), (0, 1), (0, 2)),
               ((0, 0), (1, 1), (2, 2)),
               ((1, 0), (1, 1), (1, 2)),
               ((2, 0), (2, 1), (2, 2))]

jogador = 1
vencedor = 0
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

while True:
    posicao = int(input("\nJogador {}, informe a posição desejada: ".format(jogador)))

    if posicao not in range(1, 10):
        break

    x, y = mapa[posicao]

    if tabuleiro[x][y] not in " ":
        print("A posição já está preenchida!")
        continue

    tabuleiro[x][y] = simbolos[jogador]

    mostra_tabuleiro = f'''
    {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}
   ---+---+---
    {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}
   ---+---+---
    {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} \n\n'''

    print(mostra_tabuleiro)

    for combinacao in combinacoes:
        p1, p2, p3 = combinacao

        elemento1 = tabuleiro[p1[0]][p1[1]]
        elemento2 = tabuleiro[p2[0]][p2[1]]
        elemento3 = tabuleiro[p3[0]][p3[1]]

        if " " in (elemento1, elemento2, elemento3):
            continue

        if (elemento1 == elemento2) and (elemento1 == elemento3) and (elemento2 == elemento3):
            vencedor = jogador
            break

    if vencedor > 0:
        print("O jogador {} venceu o jogo!".format(vencedor))
        break

    jogador = 2 if jogador == 1 else 1

