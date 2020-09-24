'''
    Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
    Exiba o valor do desconto e o preço a pagar.
'''
preco = float(input("Informe o preço da mercadoria: "))
percentual = int(input("Informe o percentual de desconto: "))

print("Valor da mercadoria: R$ {}, valor do desconto: R$ {}, valor a pagar: R$ {}".format(
    preco, (preco * (percentual / 100)), (preco - (preco * (percentual / 100)))))