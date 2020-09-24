'''
    Exercício 5.24 - Modifique o programa anterior de forma a ler um número n.
    Imprima os n primeiros números primos.
'''
n = int(input("Digite a quantidade de números primos a ser mostrada: "))
qtde = 0
x = 2

while qtde <= n:
    if x == 2:
        print("{} é primo!".format(x))
        qtde += 1
    elif x == 3:
        print("{} é primo!".format(x))
        qtde += 1
    else:
        if x % 2 != 0:
            primo = True
            y = 3

            while y < x:
                if x % y == 0:
                    primo = False
                y += 1

            if primo:
                print("{} é primo!".format(x))
    qtde += 1
    x += 1

