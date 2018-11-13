'''
    Exercício 6.7 - Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses
    foram abertos e fechados na ordem correta. Exemplo:

    (()) - OK
    ()()(()()) - OK
    ()) - Erro
'''
expressao = input("Digite uma expressão com parenteses: ")

pilha = []
erro = False

for item in expressao:
    if item == "(":
        pilha.append(item)
    elif item == ")":
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            erro = True

if len(pilha) == 0 and not erro:
    print("OK")
else:
    print("Erro")