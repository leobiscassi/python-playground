'''
    Exercício 6.2 - Faça um programa que leia duas listas e que gere uma terceira com
    os elementos das duas primeiras.
'''

a = []
b = []

while True:
    x = input("Digite um elemento para a lista 1 (0 para sair): ")

    if x == 0 or x == "0":
        break

    a.append(x)

while True:
    x = input("Digite um elemento para a lista 2 (0 para sair): ")

    if x == 0 or x == "0":
        break

    b.append(x)

c = a + b

print("Lista 1: {}".format(a))
print("Lista 2: {}".format(b))
print("Lista 3: {}".format(c))

