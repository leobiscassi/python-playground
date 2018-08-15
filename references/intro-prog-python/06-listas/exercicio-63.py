'''
    Exercício 6.3 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
'''
a = [1, 2, 3, 3, 4, 4, 4, 5, 10, 99, 100]
b = [666, 666, 666, 344, 567, 123, 100, 100]
c = []

for i in a:
    if i not in c:
        c.append(i)

for i in b:
    if i not in c:
        c.append(i)


print("Lista a: {}".format(a))
print("Lista b: {}".format(b))
print("Lista c: {}".format(c))

