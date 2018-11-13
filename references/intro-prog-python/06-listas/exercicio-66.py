'''
    Exercício 6.6 - Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho, considere o
    comando A para atendimento da fila 1; e B, para atendimento da fila 2. O mesmo para a chegada de clientes:
    F para a fila 1; e G, papra fila 2.
'''
ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))

while True:
    print("\nExistem {} clientes na fila 1.".format(len(fila1)))
    print("Fila 1 atual: {}".format(fila1))
    print("Fila 2 atual: {}".format(fila2))
    print("Digite F para adicionar um cliente ao fim da fila1, ")
    print("ou G para adicionar um cliente ao fim da fila2; ")
    print("A para realizar um atendimento na fila1, ")
    print("ou B para realizar um atendimento na fila2.")
    print("S para sair.")

    operacao = input("Operação (F, G, A, B ou S): ")

    if operacao == "A":
        if (len(fila1)) > 0:
            atendido = fila1.pop(0)
            print("Cliente {} atendido".format(atendido))
        else:
            print("Fila 1 vazia! Ninguém para atender.")
    elif operacao == "B":
        if (len(fila2)) > 0:
            atendido = fila2.pop(0)
            print("Cliente {} atendido".format(atendido))
        else:
            print("Fila 2 vazia! Ninguém para atender.")
    elif operacao == "F":
        ultimo1 += 1
        fila1.append(ultimo1)
    elif operacao == "G":
        ultimo2 += 1
        fila2.append(ultimo2)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, G, A, B ou S!")

