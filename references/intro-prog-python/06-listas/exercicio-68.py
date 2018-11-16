'''
    Exercício 6.8 - Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar a mesma tarefa, mas sem
    utilizar a variável achou. Dica: observe a condição de saída do while
'''
l = [15, 7, 27, 39]

p = int(input("Digite o valor a procurar: "))

x = 0

while x < len(l):
    if l[x] == p:
        break
    x += 1

if x < len(l):
    print("{} achado na posição {}".format(p, x))
else:
    print("{} não encontrado".format(p))

