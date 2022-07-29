"""
Usando o exemplo do arquivo anterior
"""

from random import randint

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # Não recebe classe nem instância (e muito menos pode utilizar ambos)
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Luiz', 32) 
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print()

p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1.get_ano_nascimento()

print(Pessoa.gera_id())  # Pode-se chamar tanto pela instância quanto pela classe. Métodos estáticos você não é obrigado a instanciar um objeto para chamar o método.
print(p1.gera_id())  
