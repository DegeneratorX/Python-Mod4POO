class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    def falar(self):
        print(f'{self.nomeclasse} está falando...')


class Cliente(Pessoa):  # Tudo que tem em Pessoa, tem em Cliente....
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')


class clienteVIP(Cliente):  # ... E tudo que tem em Cliente, tem em ClienteVIP. Logo, tudo que tem em Pessoa, tem em ClienteVIP.
    pass
