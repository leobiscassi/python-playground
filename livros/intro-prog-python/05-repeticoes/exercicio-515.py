'''
    Exercício 5.15 - Escreva um programa para controlar uma pequena máquina registradora.
    Você deve solicitar que o usuário digite o código do produto e a quantidade comprada.
    Utilize a tabela de códigos apresentada no livro (pag. 94) para obter o preço de cada produto.
    Seu programa deve exibir o total das compras depois que o usuário digitar 0.
    Qualquer outro código deve gerar uma mensagem de erro "Código inválido!".
'''
produto = 0
total_compra = 0

while True:
    produto = int(input("Digite o código do produto: "))

    if produto == 0:
        print("Total de compras: {}".format(total_compra))
        break
    elif produto == 1:
        total_compra += 0.50
    elif produto == 2:
        total_compra += 1.00
    elif produto == 3:
        total_compra += 4.00
    elif produto == 5:
        total_compra += 7.00
    elif produto == 9:
        total_compra += 8.00
    else:
        print("Código inválido!")