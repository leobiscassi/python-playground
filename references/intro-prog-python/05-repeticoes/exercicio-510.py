'''
    Exercício 5.10 - Modifique o programa da listagem 5.10 para que aceite respostas com letras
    maísculas e minúsculas em todas as questões
'''
pontos = 0
questao = 1

while questao <= 3:
    resposta = input("Resposta da questão %d: " % questao)

    if questao == 1 and resposta.lower() == "b":
        pontos += 1
    elif questao == 2 and resposta.lower() == "a":
        pontos += 1
    elif questao == 3 and resposta.lower() == "d":
        pontos += 1

    questao += 1

print("O aluno fez %d ponto(s)" % pontos)