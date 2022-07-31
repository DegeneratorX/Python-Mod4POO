from classes.conta import Conta

class ContaPoupanca(Conta): # Herdo da classe Conta tudo.
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.detalhes()
        