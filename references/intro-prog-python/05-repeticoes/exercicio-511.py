'''
    Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
    Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
'''
deposito = float(input("Informe o valor do depósito inicial: "))
taxa = float(input("Informe o valor da taxa de juros da poupança: "))

saldo = deposito
juros = 0
total_juros = 0

mes = 1

while mes <= 24:
    juros = saldo * taxa
    saldo += juros
    total_juros += juros
    print("Saldo R$ {}, mês {}".format(saldo, mes))
    mes += 1

print("O total ganho com juros no período foi de R$ {}".format(total_juros))