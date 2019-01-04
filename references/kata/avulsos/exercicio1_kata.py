'''
	Exercício - Kata #1

	Faça um programa que use a função valorPagamento para determinar o valor a ser
	pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o
	valor da prestação e o número de dias em atraso e passar estes valores para a
	função valorPagamento, que calculará o valor a ser pago e devolverá este valor
	ao programa que a chamou. O programa deverá então exibir o valor a ser pago na
	tela. Após a execução o programa deverá voltar a pedir outro valor de prestação
	e assim continuar até que seja informado um valor igual a zero para a prestação
	Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
	que conterá a quantidade e o valor total de prestações pagas no dia.
	O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos
	sem atraso, cobrar o valor da prestação. Quando houver atraso,
	cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def retorna_valor_pagamento(vl_prestacao, dias_atraso, perc_multa=0.03, perc_juros=0.001):
	vl_calculado = 0.0
	vl_multa = 0.0
	vl_juros = 0.0

	if dias_atraso == 0:
		vl_calculado = vl_prestacao
	else:
		vl_multa, vl_juros = vl_prestacao * perc_multa, vl_prestacao * (perc_juros * dias_atraso)
		vl_calculado = vl_prestacao + vl_multa + vl_juros

	return vl_calculado

def main():
	qtde_pagtos = 0
	total_pagtos = 0.0

	while True:
		vl_prestacao = float(input("Digite o valor da prestação (0 para sair): "))

		if vl_prestacao == 0.00:
			break

		dias_atraso = int(input("Digite a qtde. de dias de atraso: "))

		vl_pagamento = retorna_valor_pagamento(vl_prestacao, dias_atraso)
		qtde_pagtos += 1
		total_pagtos += vl_pagamento

		print(f"O valor a ser pago é {vl_pagamento}\n")

	print(f"Foram realizados {qtde_pagtos} pagtos no valor total de R$ {total_pagtos}")

if __name__ == "__main__":
	main()

