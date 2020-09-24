'''
    Exercício 10.11 - Altere a classe ContaEspecial de forma que seu extrato exiba o limite
    e o total disponível para saque.
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

    def __saldo_disponivel__(self, valor):
        disponivel = True if self.saldo >= valor else False

        return disponivel

    def resumo(self):
        print(f"\nCC Nº {self.numero}, saldo: {self.saldo}")
        print("\nInformações dos correntistas:\n")

        for cliente in self.clientes:
            print(f"{cliente.nome}, telefone: {cliente.telefone}")

    def saque(self, valor):
        realizado = False

        if self.__saldo_disponivel__(valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            realizado = True

        return realizado

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC {self.numero}\n")

        for op, val in self.operacoes:
            print(f"{op}: {val}")

        print(f"\nSaldo: {self.saldo}")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def __saldo_disponivel__(self, valor):
        disponivel = True if self.saldo + self.limite >= valor else False

        return disponivel

    def extrato(self):
        print(f"Extrato CC {self.numero}\n")

        for op, val in self.operacoes:
            print(f"{op}: {val}")

        print(f"\nSaldo: {self.saldo}")
        print(f"\nLimite: {self.limite}")
        print(f"\nTotal disponível para saque: {self.saldo + self.limite}")

if __name__ == '__main__':
    leo = Cliente("Léo Biscassi", "(17) 99671-3721")
    jose = Cliente("José Biscassi", "(17) 3331-4571")
    clientes = [leo, jose]

    conta = Conta(clientes, "1234-0", 1000)
    conta_especial = ContaEspecial([leo], "454-X", 1000, 2000)

    print(conta.saque(1500))
    print(conta.saque(500))
    print(conta_especial.saque(2000))
    print(conta_especial.saque(3500))
