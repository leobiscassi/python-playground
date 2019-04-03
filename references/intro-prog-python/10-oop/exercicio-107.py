'''
    Exercício 10.7 - Modique o método resumo da classe Conta para exibir o nome e
    o telefone de cada cliente.
'''
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"\nCC Nº {self.numero}, saldo: {self.saldo}")
        print("\nInformações dos correntistas:\n")

        for cliente in self.clientes:
            print(f"{cliente.nome}, telefone: {cliente.telefone}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC {self.numero}\n")

        for op, val in self.operacoes:
            print(f"{op}: {val}")

        print(f"\nSaldo: {self.saldo}")


if __name__ == '__main__':
    joao = Cliente("João da Silva", "777-1234")
    maria = Cliente("Maria Silva", "555-4321")

    conta1 = Conta([joao, maria], 1, 10)
    conta1.extrato()
    conta1.saque(5)
    conta1.extrato()
    conta1.saque(100)
    conta1.extrato()
    conta1.resumo()