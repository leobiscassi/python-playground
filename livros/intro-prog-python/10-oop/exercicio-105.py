'''
    Exercício 10.5 - Utilizando a classe Televisao modificada no exercício anterior,
    crie duas instâncias (objetos), especificando o valor de min e max por nome.
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

    tv_sala = Televisao(5, 1, 55)
    print(f"tv_sala.canal: {tv_sala.canal}")
    print(f"tv_sala.cmin: {tv_sala.cmin}")
    print(f"tv_sala.cmax: {tv_sala.cmax}")

    tv_cozinha = Televisao(1, 1, 99)
    print(f"tv_cozinha.canal: {tv_cozinha.canal}")
    print(f"tv_cozinha.cmin: {tv_cozinha.cmin}")
    print(f"tv_cozinha.cmax: {tv_cozinha.cmax}")