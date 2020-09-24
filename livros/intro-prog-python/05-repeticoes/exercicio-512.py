'''
    Exercício 5.12 - Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
    Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros no
    mês seguinte.
'''
deposito = float(input("Informe o valor do depósito inicial: "))
taxa = float(input("Informe o valor da taxa de juros da poupança: "))

saldo = deposito
juros = 0
total_juros = 0

mes = 1

while mes <= 24:
    deposito = float(input("Informe o valor do depósito: "))
    juros = saldo * taxa
    total_juros += juros
    saldo += deposito + juros
    print("Saldo R$ {}, mês {}".format(saldo, mes))
    mes += 1

print("O total ganho com juros no período foi de R$ {}".format(total_juros))