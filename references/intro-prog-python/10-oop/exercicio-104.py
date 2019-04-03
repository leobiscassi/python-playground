'''
    Exercício 10.4 - Utilizando o que aprendemos com funções, modifique o construtor da classe
    Televisao de forma que min e max sejam parâmetros opcionais, onde min vale 2 e max vale 14,
    caso outro valor não seja passado.
'''
class Televisao:
    def __init__(self, canal=2, min=2, max=14):
        self.ligada = False
        self.canal = canal
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal-1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal+1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin


if __name__ == '__main__':
    tv = Televisao()
    print(f"tv.canal: {tv.canal}")
    print(f"tv.cmin: {tv.cmin}")
    print(f"tv.cmax: {tv.cmax}")

    