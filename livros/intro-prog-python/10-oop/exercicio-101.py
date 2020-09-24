'''
    Exercício 10.1 - Adicione os atributos tamanho e marca à classe Televisao.
    Crie dois objetos Televisao e atribua tamanhos e marcas diferentes. Depois,
    imprima o valor desses atributos de forma a confirmar a independência dos valores
    de cada instância (objeto).
'''
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.marca = None
        self.tamanho = None

if __name__ == "__main__":
    tv_sala = Televisao()
    tv_sala.marca = "Toshiba"
    tv_sala.tamanho = "14'"

    tv_cozinha = Televisao()
    tv_cozinha.marca = "Samsumg"
    tv_cozinha.tamanho = "40'"

    print(f"tv_sala.marca: {tv_sala.marca}")
    print(f"tv_sala.tamanho: {tv_sala.tamanho}")
    print(f"tv_cozinha.marca: {tv_cozinha.marca}")
    print(f"tv_cozinha.tamanho: {tv_cozinha.tamanho}")

