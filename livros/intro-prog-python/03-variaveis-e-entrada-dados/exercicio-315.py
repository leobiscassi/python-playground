'''
    Exercício 3.15 - Escreva um programa para calcular a redução do tempo de vida de um fumante.
    Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
    perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
'''
cigarros = int(input("Quantidade de cigarros por dia: "))
anos = int(input("Há quantos anos fuma: "))
total_cigarros = (anos * 365) * cigarros
#  total de minutos perdidos (total_cigarros * 10), dividos pela qtde total de minutos de um dia
dias_perdidos = (total_cigarros * 10) / 1440

print("Você já perdeu {} dias de vida.".format(dias_perdidos))