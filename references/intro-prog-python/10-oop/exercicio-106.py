'''
    Exercício 10.6 - Altere o programa de forma que a mensagem saldo insuficiente
    seja exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível.
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
        print(f"CC Nº {self.numero}, saldo: {self.saldo}")

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

    conta1 = Conta([joao], 1, 10)
    conta1.extrato()
    conta1.saque(5)
    conta1.extrato()
    conta1.saque(100)
    conta1.extrato()