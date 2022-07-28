"""
SETTER = CONFIGURANDO UM VALOR (=)
GETTER = OBTER UM VALOR (.)
"""

class Pessoa1:
    def nome(self):
        return 'Victor'


p1 = Pessoa1()
print(p1.nome())  # Aqui basicamente executa o método




class Pessoa2:
    @property  # Ao colocar "@property", indica pro python que a função abaixo agora vira um atributo da classe, não como um método...
    def nome(self):
        return 'Victor'


p2 = Pessoa2()
print(p2.nome)  # ...e por isso, agora não se usa mais (), pois será passado o valor que foi retornado, e não o método em si. Meio que com (), seria 'Victor'(), e ocasiona em erro.
