'''
    Exercício 6.9 - Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v
    que também será procurado. Na impressão, indique qual dos dois valores foi achado primeiro.
'''
l = [15, 7, 27, 39]

p = int(input("Digite o valor p a procurar: "))
v = int(input("Digite o valor v a procurar: "))
achou = ""

x = 0
while x < len(l):
    if l[x] == p:
        achou = "p"
        break
    elif l[x] == v:
        achou = "v"
        break
    x += 1

if achou == "p":
    print("{} achado na posição {}".format(p, x))
elif achou == "v":
    print("{} achado na posição {}".format(v, x))
else:
    print("{} e {} não foram encontrados".format(p, v))