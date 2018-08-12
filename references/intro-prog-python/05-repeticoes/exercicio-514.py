'''
    Exercício 5.14 - Escreva um programa que leia números inteiros do teclado.
    O programa deve ler os números até que o usuário digite 0. No final da execução, exiba a quantidade de
    números digitados, assim como a soma e a média aritimética.
'''
n = 0
qtde = 0
soma = 0

while True:
    n = int(input("Digite um número: "))

    if n == 0:
        print("Qtde. {}, Soma {}, Média {}".format(qtde, soma, soma / qtde))
        break
    else:
        qtde += 1
        soma += n

