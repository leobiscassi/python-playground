'''
    Exercício 5.13 - Escreva um programa que pergunte o valor inicial de uma divida e o juro mensal.
    Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga,
    o total pago e o total de juros pagos.
'''
divida = float(input("Digite o valor da dívida: "))
taxa_juros = float(input("Digite a taxa de juros: "))
pagto_mensal = float(input("Digite o pagto. mensal: "))

meses = 1
total_pago = divida
juros = 0
total_juros = 0
troco = 0

while divida > 0:
    juros = divida * taxa_juros
    total_juros += juros
    total_pago += juros
    divida += juros

    if divida < pagto_mensal:
        troco = pagto_mensal - divida
        divida = 0
    else:
        divida -= pagto_mensal

    meses += 1

print("Qtde. de meses {}, total pago R$ {}, total juros R$ {}, troco da ultima parcela R$ {}"\
      .format(meses, total_pago, total_juros, troco))