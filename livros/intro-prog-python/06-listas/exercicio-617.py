'''
    Exercício 6.17 - Altere o programa da listagem 6.53 de forma a solicitar ao usuário o produto e a
    quantidade vendida. Verifique se o nome do produto digitado existe no dicionário, e só então efetue
    a baixa em estoque.
'''
estoque = {"tomate" : [1000, 2.30],
           "alface" : [500, 0.45],
           "batata" : [2001, 1.20],
           "feijão" : [100, 1.50]}

venda = []

while True:
    print("\nInforme o produto e a quantidade, fim para terminar")
    produto = input("Digite o produto: ")

    if produto == "fim":
        break

    quantidade = int(input("Digite a quantidade: "))

    venda.append([produto, quantidade])

total = 0

print("Vendas:\n")

for operacao in venda:
    produto, quantidade = operacao

    if produto in estoque:
        preco = estoque[produto][1]
        custo = quantidade * preco

        print("{}: {} x {} = {}".format(produto, quantidade, preco, custo))

        estoque[produto][0] -= quantidade
        total += custo
    else:
        print("\nProduto '{}' não encontrado!".format(produto))

print("\nCusto total: {}".format(total))
print("\nEstoque:\n")

for chave, dados in estoque.items():
    print("Descrição: {}".format(chave))
    print("Quantidade: {}".format(dados[0]))
    print("Valor: {}".format(dados[1]))

