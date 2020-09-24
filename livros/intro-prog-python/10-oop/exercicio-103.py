'''
    Exercício 10.3 - Modique a classe Televisao de forma que, se pedirmos para
    mudar o canal para baixo, além do mínimo, ela vá para o canal máximo. Se
    mudarmos para cima, além do canal máximo, que volte ao canal mínimo.
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
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal+1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin


if __name__ == '__main__':
    tv = Televisao(10, 2, 10)
    print(f"tv.canal: {tv.canal}")
    tv.muda_canal_para_cima()
    print(f"tv.canal: {tv.canal}")
    
