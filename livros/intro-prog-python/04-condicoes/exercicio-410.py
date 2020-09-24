'''
    Exercício 4.10 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
    Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para industriais e
    C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir [checar no livro].
'''
quantidade = int(input("Qual a quantidade de kWh consumida? "))
tipo = input("Qual o tipo de instalação? ")
preco = 0

if tipo == "R":
    if quantidade <= 500:
        preco = quantidade * 0.40
    else:
        preco = quantidade * 0.65
elif tipo == "C":
    if quantidade <= 1000:
        preco = quantidade * 0.55
    else:
        preco = quantidade * 0.60
else:
    if quantidade <= 5000:
        preco = quantidade * 0.55
    else:
        preco = quantidade * 0.60

print("O valor a ser pago é de R$ {}".format(preco))

