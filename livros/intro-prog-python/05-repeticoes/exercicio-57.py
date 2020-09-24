'''
    Exercício 5.7 - Modifique o programa anterior de forma que o usuário também digite o início e o fim
    da tabuada, em vez de começar com 1 e 10.
'''
n = int(input("Tabuada de: "))
inicio = int(input("Inicio da tabuada: "))
fim = int(input("Fim da tabuada: "))

while inicio <= fim:
    print("{} x {} = {}".format(n, inicio, n * inicio))
    inicio += 1

