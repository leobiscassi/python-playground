'''
    Exercício 8.13 - Altere o programa da listagem 8.37 de forma que o usuário tenha três chances de acertar o
    número. O programa termina se o usuário acertar ou errar três vezes.
'''
import random

t = 3
i = 0

while i < t:
    n = random.randint(1, 10)
    x = int(input("Escolha um número entre 1 e 10: "))

    if x == n:
        print("Você acertou!")
    else:
        print("Você errou.")

    i += 1

    if (t - i) > 0:
        print("\nVocê ainda possui {} tentativas!".format(t - i))
    else:
        print("\nO número de tentativas esgotou!")

