from classes.conta import Conta

class ContaCorrente(Conta):  # Herdo da classe Conta tudo.
    def __init__(self, agencia, conta, saldo, limite=100):  # Por padrão, mesmo que não mande um limite, virá um limite de 100 reais
        super().__init__(agencia, conta, saldo)  # Atribuição dos valores instanciados para o construtor da classe Conta
        self._limite = limite  # Atribuição do valor limite a partir da instância. É um atributo exclusivo de conta corrente.

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.detalhes()
