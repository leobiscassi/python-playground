'''
    Exercício 5.21 - Reescreva o programa da listagem 5.14 de forma a continuar executando até que
    o valor digitado seja 0. Utilize repetições aninhadas.
'''
while True:
    valor = float(input("\nDigite o valor a pagar: "))

    if valor == 0:
        print("Programa sendo encerrado ...")
        break

    cedulas = 0
    atual = 100
    apagar = valor

    while True:
        if atual <= round(apagar, 2):
            apagar -= atual
            cedulas += 1
        else:
            if cedulas != 0:
                print("%d cédula(s) de R$ %.2f" % (cedulas, atual))

            if round(apagar, 2) == 0.00:
                break

            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01

            cedulas = 0

