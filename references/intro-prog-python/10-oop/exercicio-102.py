'''
    Exercício 10.2 - Atualmente, a classe Televisao inicializa o canal com 2.
    Modique a classe Televisao de forma a receber o canal inicial em seu construtor.
'''
class Televisao:
    def __init__(self, canal, min, max):
        self.ligada = False
        self.canal = canal
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal-1 >= self.cmin:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal+1 <= self.cmax:
            self.canal += 1


if __name__ == '__main__':
    tv = Televisao(10, 1, 99)
    print(f"tv.canal: {tv.canal}")