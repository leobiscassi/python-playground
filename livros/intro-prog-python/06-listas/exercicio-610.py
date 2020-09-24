'''
    Exercício 6.10 - Modifique o programa do exercício 6.9 de forma a pesquisar p e v em toda
    a lista e informando o usuário a posição onde p e a posição onde v foram encontrados.
'''
l = [15, 7, 27, 39]

p = int(input("Digite o valor p a procurar: "))
v = int(input("Digite o valor v a procurar: "))
posicao_p = None
posicao_v = None

x = 0
while x < len(l):
    if l[x] == p:
        posicao_p = x
    elif l[x] == v:
        posicao_v = x
    x += 1

if not posicao_v is None and not posicao_p is None:
    print("{} encontrado na posição {} e {} encontrado na posição {}".format(p, posicao_p, v, posicao_v))
elif not posicao_v is None:
    print("{} encontrado na posição {} e {} não encontrado".format(v, posicao_v, p))
elif not posicao_p is None:
    print("{} encontrado na posição {} e {} não encontrado".format(p, posicao_p, v))
else:
    print("{} e {} não foram encontrados".format(p, v))

