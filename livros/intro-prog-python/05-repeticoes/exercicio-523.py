'''
    Exercício 5.23 - Escreva um programa que leia um número e verifique se é ou não
    um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2
    e depois por todos os números impares até o número lido. Se o resto de uma dessas divisões for igual
    a zero, o número não é primo. Observer que 0 e 1 não são primos e que 2 é o único número primo que é par.
'''
numero = int(input("Digite um número: "))
primo = True

if numero % 2 != 0:
    x = 3

    while x <= numero:
        if x % 2 != 0:
            if numero != x and numero % x == 0:
                primo = False
        x += 1
else:
    primo = False

if primo:
    print("O número {} é primo!".format(numero))
else:
    print("O número {} não é primo!".format(numero))

