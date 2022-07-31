from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia  # Protejo os valores, pois não tem necessidade de alterar eles fora da classe.
        self._conta = conta
        self._saldo = saldo  # Esse tem necessidade, mas apenas para ver se o valor inserido foi um inteiro ou float e depois atualizar com novo saldo. Por isso se usa setter.


    @property
    def agencia(self):  # Consulta da agência. Posso consultar fora da classe mesmo com valores protected chamando essa função a partir da instância, mas sem parênteses. Ex: print(cp.agencia)
        return self._agencia


    @property
    def conta(self):  # Consulta da conta
        return self._agencia


    @property
    def saldo(self):  # Consulta do saldo
        return self._saldo


    @saldo.setter
    def saldo(self, valor):  # Toda conta tem um saldo, a consulta é sem limitações. Uso setter pois irei modificar o valor do saldo.
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico")
        self._saldo = valor


    def depositar(self, valor):  # Toda conta tem um depósito, e sem limitações pra depósito
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")
        
        self.saldo += valor
        self.detalhes()

    
    def detalhes(self):  # Mostra detalhes apenas
        print(f"Agência: {self.agencia}", end = ' ')
        print(f"Conta: {self.conta}", end = ' ')
        print(f"Saldo: {self.saldo}")

    @abstractmethod  # Forçando para que as classes filhas tenham esse método aqui, pois toda conta tem um saque. Porém, funcionam de forma diferente pra cada classe.
    def sacar(self, valor):  # A forma de saque pra conta corrente e conta poupança são diferentes, existem limitações.
        pass
