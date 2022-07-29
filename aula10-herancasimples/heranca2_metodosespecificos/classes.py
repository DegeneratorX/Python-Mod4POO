"""
Também é possível definir métodos específicos para cada subclasse
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f"{self.nomeclasse} está falando...")


class Cliente(Pessoa):  # Herdou TUDO de Pessoa.
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')


class Aluno(Pessoa):  # Herdou TUDO de Pessoa.
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')

# Ou seja, as subclasses herdam (herança) o método "falar", mas a superclasse não herda "estudar" nem "comprar".
# A herança sempre é de cima pra baixo.
