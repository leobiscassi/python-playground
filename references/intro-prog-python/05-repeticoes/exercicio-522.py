'''
    Exercício 5.22 - Escreva um programa que exiba uma lista de opções (menu): adição,
    subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
    Repita até que a opção sair seja escolhida.
'''
while True:
    print("\n**********************************************")
    print("\t\t\tPROGRAMA DE TABUADA\t\t\t")
    print("**********************************************")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")
    print("0. Sair\n")
    opcao = int(input("Digite o número da opção escolhida: "))

    if opcao == 0:
        break

    numero = int(input("Digite um número: "))
    x = numero

    while x >= 1:
        if opcao == 1:
            print("{} + {} = {}".format(numero, x, numero + x))
        elif opcao == 2:
            print("{} - {} = {}".format(numero, x, numero - x))
        elif opcao == 3:
            print("{} / {} = {}".format(numero, x, numero / x))
        else:
            print("{} * {} = {}".format(numero, x, numero * x))
        x -= 1