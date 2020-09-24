'''
    Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.
    Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''
distancia = int(input("Informe a distância a ser percorrida em KM: "))
velocidade_media = float(input("Informe a velocidade média esperada em KM/h: "))

print("O tempo de viagem será de {} horas.".format(distancia / velocidade_media))
