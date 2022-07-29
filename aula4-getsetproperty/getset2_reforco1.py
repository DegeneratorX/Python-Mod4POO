"""
SETTER = CONFIGURANDO UM VALOR (=)
GETTER = OBTER UM VALOR (.)
"""

class Pessoa1:
    def nome(self):
        return 'Victor'


p1 = Pessoa1()
print(p1.nome())  # Aqui basicamente executa o método

#####################################################################
print()
print("#"*30)
print()

class Pessoa2:
    @property  # Ao colocar "@property", indica pro python que a função abaixo agora vira um atributo da classe, não age mais como um método...
    def nome(self):
        return 'Victor'


p2 = Pessoa2()
print(p2.nome)  # ...e por isso, agora não se usa mais (), pois será passado o valor que foi retornado, e não o método em si. Meio que com (), seria 'Victor'(), e ocasiona em erro.

# Exemplo de aplicação: Vamos supor que tenha 3000 pessoas definidas em várias partes de um programa vindas da mesma classe.
# E vamos supor que eu quero editar o nome de algumas pessoas.
# É mais fácil eu editar os nomes pelo p1.nome em todos os lugares do código fora da classe, 
# ou é melhor eu usar um getter e editar somente os nomes necessários dentro da classe?

# E pra gettar e editar (settar), eu simplesmente faço isso:
#####################################################################
print()
print("#"*30)
print()

class Pessoa3:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        # Este código é executado quando alguém for ler o valor de self.nome
        return self._nome

    @nome.setter
    def nome(self, valor):
        # Este código é executado sempre que alguém fizer self._nome = valor
        self._nome = valor

p3 = Pessoa3('Victor')
print(f"p3.nome: {p3.nome} / p3._nome: {p3._nome}")

p3.nome = 'Martins'

print(f"Novo p3.nome: {p3.nome} / Novo p3._nome: {p3._nome}")
