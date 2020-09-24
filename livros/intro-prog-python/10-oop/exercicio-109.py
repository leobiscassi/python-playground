'''
    Exercício 10.9 - Crie classes para representar estados e cidades. Cada estado tem um nome, sigla e
    cidades. Cada cidade tem nome e população. Escreva um programa de testes que crie três estados com algumas
    cidades em cada um. Exiba a população de cada estado como a soma da população de suas cidades.
'''
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def calcula_populacao(self):
        populacao = 0
        for cidade in self.cidades:
            populacao += cidade.populacao

        return populacao


if __name__ == '__main__':
    guaira = Cidade("Guaíra", 40000)
    barretos = Cidade("Barretos", 120000)
    sp = Estado("São Paulo", "SP", [guaira, barretos])

    print(f"{sp.nome}, população: {sp.calcula_populacao()}")

