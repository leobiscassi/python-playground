'''
    Exercício 6.5 - Altere o programa da listagem 6.21 de forma a poder trabalhar com vários comandos digitados de uma
    vez só. Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma
    string.

    Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do
    programa.
'''
ultimo = 10
fila = list(range(1, ultimo + 1))
encerra = False

while True:
    print("\nExistem {} clientes na fila".format(len(fila)))
    print("Fila atual: {}".format(fila))

    if encerra: break

    print("Digite F para adicionar um cliente ao fim da fila, ")
    print("ou A papra realizar o atendimento. S para sair.")

    operacao = input("Operação (F, A ou S): ")

    for item in operacao:
        if item == "A":
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print("Cliente {} atendido".format(atendido))
            else:
                print("Fila vazia! Ninguém para atender.")
        elif item == "F":
            ultimo += 1
            fila.append(ultimo)
        elif item == "S":
            encerra = True
        else:
            print("Operação inválida! Digite apenas F, A ou S!")

