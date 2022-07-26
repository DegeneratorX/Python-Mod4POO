"""
Método de classe trabalha com classes apenas (antes de criar uma instância)
Métodos de instância trabalha com classes e instâncias
"""

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):           # <- Métodos de instância, que trabalham com a instância em si
        print(self.ano_atual - self.idade)

    @classmethod  # Decorador que transforma o método em um método de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):  # Como o método é de classe, não de instância, passa a usar "cls" como convenção, ao invés de self.
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa('Luiz', 32)  # Normalmente o que se passa
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print()

p1 = Pessoa.por_ano_nascimento('Luiz', 1987)  # Alternativa como forma de mostrar a idade
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

# Métodos de classe é uma forma alternativa de buscar valores passando como parâmetros outras informações
# O método de classe retorna um objeto da classe em si. (Factory, fabrica um objeto)
