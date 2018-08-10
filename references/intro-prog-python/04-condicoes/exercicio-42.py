'''
    4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h,
    exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando
    R$ 5 por km acima de 80 km/h.
'''
velocidade = int(input("Qual a velocidade do carro em km/h? "))

if velocidade > 80:
    print("O valor da multa é R$ {}".format((velocidade - 80) * 5))

